package demo;

import org.docx4j.XmlUtils;
import org.docx4j.wml.*;

import java.math.BigInteger;

/** JAXB in docx4j: XML text <-> generated Java classes, both directions. */
public class JaxbBasics {
    static final String W = "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\"";

    public static void main(String[] args) throws Exception {
        // 1. Unmarshal: XML -> typed objects (org.docx4j.wml.P was generated from the OOXML schema)
        String xml = "<w:p " + W + ">"
                + "<w:pPr><w:pStyle w:val=\"Heading1\"/><w:outlineLvl w:val=\"0\"/></w:pPr>"
                + "<w:r><w:t>Hello JAXB</w:t></w:r></w:p>";
        P p = (P) XmlUtils.unmarshalString(xml);

        System.out.println("style      = " + p.getPPr().getPStyle().getVal());
        System.out.println("outlineLvl = " + p.getPPr().getOutlineLvl().getVal());
        R r = (R) p.getContent().get(0);
        Text t = (Text) XmlUtils.unwrap(r.getContent().get(0));   // <w:t> arrives wrapped in JAXBElement
        System.out.println("text       = " + t.getValue());

        // 2. Build objects in Java (ObjectFactory is generated too), then marshal: objects -> XML
        ObjectFactory f = new ObjectFactory();
        P p2 = f.createP();
        PPr ppr = f.createPPr();
        PPrBase.OutlineLvl lvl = f.createPPrBaseOutlineLvl();
        lvl.setVal(BigInteger.valueOf(1));
        ppr.setOutlineLvl(lvl);
        p2.setPPr(ppr);
        R r2 = f.createR();
        Text t2 = f.createText();
        t2.setValue("Built in Java");
        r2.getContent().add(f.createRT(t2));
        p2.getContent().add(r2);

        System.out.println(XmlUtils.marshaltoString(p2, true, true));
    }
}
