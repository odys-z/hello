package demo;

import java.io.File;
import java.math.BigInteger;
import java.util.*;


import org.docx4j.XmlUtils;
import org.docx4j.jaxb.Context;
import org.docx4j.model.PropertyResolver;
import org.docx4j.model.listnumbering.Emulator;
import org.docx4j.openpackaging.packages.WordprocessingMLPackage;
import org.docx4j.openpackaging.parts.Part;
import org.docx4j.openpackaging.parts.PartName;
import org.docx4j.openpackaging.parts.JaxbXmlPart;
import org.docx4j.openpackaging.parts.WordprocessingML.MainDocumentPart;
import org.docx4j.wml.*;

/**
 * docx4j demo, three parts:
 *   1. JAXB round trip: Java object -> XML, XML -> Java object.
 *   2. Package inventory: every part in the zip, typed (JAXB) or binary.
 *   3. Facts walker + tree: per-block facts (style, effective outline level,
 *      numbering label, table spans, source path) and a heading tree as JSON.
 *
 * Usage: mvn -q compile exec:java -Dexec.args="samples/tricky.docx"
 */
public class FactsDemo {

    public static void main(String[] args) throws Exception {
        File in = new File(args.length > 0 ? args[0] : "samples/tricky.docx");
        WordprocessingMLPackage pkg = WordprocessingMLPackage.load(in);

        jaxbRoundTrip();
        inventory(pkg);

        FactsDemo walker = new FactsDemo(pkg);
        walker.walk(pkg.getMainDocumentPart().getContent(), "body");
        System.out.println("\n== 3. Facts ==");
        for (Block b : walker.blocks) System.out.println(b.factLine());
        System.out.println("\n== 4. Tree (JSON) ==");
        System.out.println(toJson(buildTree(walker.blocks), 0));
    }

    // ------------------------------------------------------------ 1. JAXB
    static void jaxbRoundTrip() throws Exception {
        System.out.println("== 1. JAXB round trip ==");
        ObjectFactory f = Context.getWmlObjectFactory();

        // Build <w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Hello</w:t></w:r></w:p>
        P p = f.createP();
        PPr ppr = f.createPPr();
        PPrBase.PStyle ps = f.createPPrBasePStyle();
        ps.setVal("Heading1");
        ppr.setPStyle(ps);
        p.setPPr(ppr);
        R r = f.createR();
        Text t = f.createText();
        t.setValue("Hello");
        r.getContent().add(f.createRT(t));   // <w:t> is a JAXBElement<Text> inside the run
        p.getContent().add(r);

        String xml = XmlUtils.marshaltoString(p, true, true) ;   // Java -> XML
        System.out.println(xml);

        P back = (P) XmlUtils.unmarshalString(xml);              // XML -> Java
        System.out.println("unmarshalled style = " + back.getPPr().getPStyle().getVal());
    }

    // ------------------------------------------------------------ 2. Inventory
    static void inventory(WordprocessingMLPackage pkg) {
        System.out.println("\n== 2. Package parts ==");
        TreeMap<String, Part> sorted = new TreeMap<>();
        for (Map.Entry<PartName, Part> e : pkg.getParts().getParts().entrySet())
            sorted.put(e.getKey().getName(), e.getValue());
        sorted.forEach((name, part) -> System.out.printf("  %-34s %-6s %s%n",
                name, part instanceof JaxbXmlPart ? "JAXB" : "binary",
                part.getClass().getSimpleName()));
    }

    // ------------------------------------------------------------ 3. Facts
    final WordprocessingMLPackage pkg;
    final PropertyResolver resolver;
    final Map<String, Style> stylesById = new HashMap<>();
    final List<Block> blocks = new ArrayList<>();

    FactsDemo(WordprocessingMLPackage pkg) throws Exception {
        this.pkg = pkg;
        MainDocumentPart mdp = pkg.getMainDocumentPart();
        this.resolver = mdp.getPropertyResolver();
        for (Style s : mdp.getStyleDefinitionsPart().getJaxbElement().getStyle())
            stylesById.put(s.getStyleId(), s);
    }

    /** Walk block-level content in document order. src = path back into the source. */
    void walk(List<Object> content, String src) {
        for (int i = 0; i < content.size(); i++) {
            Object o = XmlUtils.unwrap(content.get(i));   // strips JAXBElement wrappers
            String here = src + "/" + i;
            if (o instanceof P p) {
                blocks.add(paragraph(p, here));
            } else if (o instanceof Tbl tbl) {
                blocks.add(table(tbl, here));
            } else if (o instanceof SdtBlock sdt) {          // content control: recurse
                walk(sdt.getSdtContent().getContent(), here + "/sdt");
            }
            // sectPr, bookmarks, altChunk (CTAltChunk) etc. would be handled here
        }
    }

    Block paragraph(P p, String src) {
        Block b = new Block("p", src);
        PPr direct = p.getPPr();
        b.styleId = (direct != null && direct.getPStyle() != null)
                ? direct.getPStyle().getVal() : "Normal";
        Style st = stylesById.get(b.styleId);
        b.styleName = (st != null && st.getName() != null) ? st.getName().getVal() : b.styleId;
        b.text = text(p);

        // (a) docx4j's resolver: merges doc defaults + style basedOn chain + direct pPr
        PPr eff = resolver.getEffectivePPr(direct);
        b.outlineResolver = outline(eff);
        // (b) explicit resolution, same precedence, written out so you can see the rule
        b.outlineManual = outline(direct);
        String chain = b.styleId;
        for (int guard = 0; b.outlineManual == null && chain != null && guard < 20; guard++) {
            Style s = stylesById.get(chain);
            if (s == null) break;
            b.outlineManual = outline(s.getPPr());
            chain = s.getBasedOn() != null ? s.getBasedOn().getVal() : null;
        }
        b.outline = b.outlineManual != null ? b.outlineManual : b.outlineResolver;
        if (b.outline == null && "Title".equals(b.styleId)) b.outline = -1;  // above level 1

        // Numbering label as Word would render it ("1.", "a)", ...). Stateful: call in order.
        PPrBase.NumPr numPr = eff != null ? eff.getNumPr() : null;
        if (numPr != null && numPr.getNumId() != null) {
            String ilvl = numPr.getIlvl() != null ? numPr.getIlvl().getVal().toString() : "0";
            try {
                Emulator.ResultTriple rt = Emulator.getNumber(pkg, b.styleId,
                        numPr.getNumId().getVal().toString(), ilvl);
                if (rt != null) b.numLabel = rt.getNumString();
            } catch (Exception e) { b.numLabel = "?"; }
        }
        return b;
    }

    static Integer outline(PPr ppr) {
        if (ppr == null || ppr.getOutlineLvl() == null) return null;
        BigInteger v = ppr.getOutlineLvl().getVal();
        return (v == null || v.intValue() >= 9) ? null : v.intValue();   // 9 = body text
    }

    Block table(Tbl tbl, String src) {
        Block b = new Block("table", src);
        List<String> rows = new ArrayList<>();
        for (Object ro : tbl.getContent()) {
            if (!(XmlUtils.unwrap(ro) instanceof Tr tr)) continue;
            List<String> cells = new ArrayList<>();
            for (Object co : tr.getContent()) {
                if (!(XmlUtils.unwrap(co) instanceof Tc tc)) continue;
                String cell = text(tc);
                TcPr pr = tc.getTcPr();
                if (pr != null && pr.getGridSpan() != null)
                    cell += " {colspan=" + pr.getGridSpan().getVal() + "}";
                if (pr != null && pr.getVMerge() != null)   // val "restart" starts; null continues
                    cell += pr.getVMerge().getVal() == null ? " {vmerge-cont}" : " {vmerge-start}";
                cells.add(cell);
            }
            rows.add(String.join(" | ", cells));
        }
        b.text = String.join(" // ", rows);
        b.hasSpans = b.text.contains("{colspan") || b.text.contains("{vmerge");
        return b;
    }

    /** Concatenate w:t text under any node: runs, hyperlinks, inline sdt, cells. */
    static String text(Object node) {
        StringBuilder sb = new StringBuilder();
        collect(node, sb);
        return sb.toString().trim();
    }
    static void collect(Object o, StringBuilder sb) {
        o = XmlUtils.unwrap(o);
        if (o instanceof Text t) sb.append(t.getValue());
        else if (o instanceof R.Tab) sb.append('\t');
        else if (o instanceof SdtElement se && se.getSdtContent() != null)
            for (Object c : se.getSdtContent().getContent()) collect(c, sb);
        else if (o instanceof ContentAccessor ca) {
            if (o instanceof Tc && sb.length() > 0) sb.append(' ');
            for (Object c : ca.getContent()) collect(c, sb);
        }
    }

    // ------------------------------------------------------------ 4. Tree
    static class Block {
        final String kind, src;
        String styleId, styleName, text, numLabel;
        Integer outlineResolver, outlineManual, outline;
        boolean hasSpans;
        final List<Block> children = new ArrayList<>();
        Block(String kind, String src) { this.kind = kind; this.src = src; }

        boolean isHeading() { return outline != null; }
        int level() { return outline + 1; }   // OOXML outline 0 = heading level 1; Title = 0

        String factLine() {
            return String.format("  %-14s %-5s style=%-10s name=%-10s outline(resolver=%s, manual=%s)%s  \"%s\"",
                    src, kind, styleId, styleName, outlineResolver, outlineManual,
                    numLabel != null ? " num=" + numLabel : "", text);
        }
    }

    /** Stack-based: a heading pops until the top is shallower, then nests. */
    static Block buildTree(List<Block> blocks) {
        Block root = new Block("root", "");
        root.outline = -2;
        Deque<Block> stack = new ArrayDeque<>();
        stack.push(root);
        for (Block b : blocks) {
            if (b.isHeading()) {
                while (stack.peek() != root && stack.peek().outline >= b.outline) stack.pop();
                stack.peek().children.add(b);
                stack.push(b);
            } else {
                stack.peek().children.add(b);
            }
        }
        return root;
    }

    static String toJson(Block b, int ind) {
        String pad = "  ".repeat(ind);
        StringBuilder sb = new StringBuilder(pad).append("{\"kind\":\"").append(b.kind).append('"');
        if (!b.src.isEmpty()) sb.append(",\"src\":\"").append(b.src).append('"');
        if (b.isHeading() && !"root".equals(b.kind)) sb.append(",\"level\":").append(b.level());
        if (b.styleId != null) sb.append(",\"style\":\"").append(esc(b.styleName)).append('"');
        if (b.numLabel != null) sb.append(",\"num\":\"").append(esc(b.numLabel)).append('"');
        if ("table".equals(b.kind)) sb.append(",\"tableKind\":\"").append(b.hasSpans ? "layout" : "data").append('"');
        if (b.text != null) sb.append(",\"text\":\"").append(esc(b.text)).append('"');
        if (!b.children.isEmpty()) {
            sb.append(",\"children\":[\n");
            for (int i = 0; i < b.children.size(); i++)
                sb.append(toJson(b.children.get(i), ind + 1)).append(i < b.children.size() - 1 ? ",\n" : "\n");
            sb.append(pad).append(']');
        }
        return sb.append('}').toString();
    }
    static String esc(String s) {
        return s.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\t", "\\t");
    }
}
