package io.odysz.ext.bisheng;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.files.FileHandle;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.VertexAttributes.Usage;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.TextureAtlas.AtlasRegion;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.graphics.g3d.Material;
import com.badlogic.gdx.graphics.g3d.Model;
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder;
import com.badlogic.gdx.graphics.g3d.utils.MeshPartBuilder.VertexInfo;
import com.badlogic.gdx.graphics.g3d.utils.ModelBuilder;
import com.badlogic.gdx.utils.Disposable;
import com.badlogic.gdx.utils.GdxRuntimeException;
import com.badlogic.gdx.utils.StreamUtils;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Created by ody on 6/13/17.
 */

public class GlyphLib implements Disposable {
	static private final int LOG2_PAGE_SIZE = 9;
	static private final int PAGE_SIZE = 1 << LOG2_PAGE_SIZE;
	//static private final int PAGES = 0x10000 / PAGE_SIZE;
    static private final int PAGES = 1;

	final FontData data;
    /** texture region, in page order */
	// Array<TextureRegion> regions;

   @Override
    public void dispose() {
       System.out.println("TODO dispose...");
   }

	public GlyphLib (FileHandle fontFile, boolean flip) {
		data = new FontData(fontFile, flip);
		//ownsTexture = true;
	}

	/**Vertex infomation*/
	private static VertexInfo[] vis;

    /**Bind string characters as a text line (page?) - the frame for printing.<br>
     * Set uv of texture page to vertex info.
     * @param str
     * @param color
     * @param texId OpenGL texture id, parameter of GL20.glActiveTexture(int)
     * @return
     */
	public Model bindFrame(String str, Color color, int texId) {
		char ch = str.charAt(0);
		Glyph glyph = data.getGlyph(ch);

		int x = glyph.xoffset;
		int y = glyph.yoffset;
		x = 10; y = 10; // debug

		float width = glyph.width, height = glyph.height;
		final float u = glyph.u, u2 = glyph.u2, v = glyph.v, v2 = glyph.v2;
        // FIXME calculate width of the string
		final float x2 = x + width, y2 = y + height;

		if (vis == null) {
			vis = new VertexInfo[4];
			for (int i = 0; i < 4; i++)
				vis[i] = new VertexInfo();
		}
		
		vis[0].setPos(x , y , 0).setCol(color).setUV(u , v );
		vis[1].setPos(x , y2, 0).setCol(Color.RED).setUV(u , v2);
		vis[2].setPos(x2, y2, 0).setCol(Color.GREEN).setUV(u2, v2);
		vis[3].setPos(x2, y , 0).setCol(Color.BLUE).setUV(u2, v );
		
        ModelBuilder modelBuilder = new ModelBuilder();
        modelBuilder.begin();
        MeshPartBuilder mpbuilder = modelBuilder.part("bisheng",
                GL20.GL_TRIANGLES, Usage.Position | Usage.ColorUnpacked | Usage.TextureCoordinates | Usage.Normal,
                new Material());
        mpbuilder.rect(vis[0], vis[1], vis[2], vis[3]);
        Model model = modelBuilder.end();
        model.calculateTransforms();

        // bind texture
        data.regions[glyph.page].getTexture().bind(texId);

        return model;
	}

    /**
     * Manager of font file - glyphs info and textures
     */
    public static class FontData {
        public float padTop, padRight, padBottom, padLeft;
        public float lineHeight;
        public String[] imagePaths;
        /** texture region, in page order */
        public TextureRegion[] regions;
        /** The glyph to display for characters not in the font. May be null. */
        public Glyph missingGlyph;
        protected Glyph[][] glyphs;
        /** The distance from the bottom of the glyph that extends the lowest to the baseline. This number is negative. */
        public float descent;
        /** The distance from the top of most uppercase characters to the baseline. Since the drawing position is the cap height of
	    * the first line, the cap height can be used to get the location of the baseline. */
        public float capHeight = 1;
        /** The distance from the cap height to the top of the tallest glyph. */
        public float ascent;
        public float down;

        /** The width of the space character. */
        public float spaceWidth;
        /** The x-height, which is the distance from the top of most lowercase characters to the baseline. */
        public float xHeight = 1;

        /** Additional characters besides whitespace where text is wrapped. Eg, a hypen (-). */
        public char[] breakChars;
        public char[] xChars = {'x', 'e', 'a', 'o', 'n', 's', 'r', 'c', 'u', 'm', 'v', 'w', 'z'};
        public char[] capChars = {'M', 'N', 'B', 'D', 'C', 'E', 'F', 'K', 'A', 'G', 'H', 'I', 'J',
                'L', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

        public FontData (FileHandle fontFile, boolean flip) {
            load(fontFile, flip);
        }

        /**Parse .fnt file, load images, (kerning disabled,)
         * handle some special chars' height (to be undersand yet).
         * Parsing results are set in glyphs, images are loaded as textures.
         * @param fontFile
         * @param flip
         */
        protected void load (FileHandle fontFile, boolean flip) {
            if (imagePaths != null) throw new IllegalStateException("Already loaded.");

            BufferedReader reader = new BufferedReader(new InputStreamReader(fontFile.read()), 512);
            try {
                // info face="Verdana" size=39 bold=0 italic=0 charset="" unicode=0 \
                // stretchH=100 smooth=1 aa=1 padding=4,4,4,4 spacing=-8,-8
                String line = reader.readLine();
                if (line == null) throw new GdxRuntimeException("Font info is missing");

                line = line.substring(line.indexOf("padding=") + 8);
                String[] padding = line.substring(0, line.indexOf(' ')).split(",", 4);
                if (padding.length != 4) throw new GdxRuntimeException("Invalid padding.");

                padTop = Integer.parseInt(padding[0]);
                padLeft = Integer.parseInt(padding[1]);
                padBottom = Integer.parseInt(padding[2]);
                padRight = Integer.parseInt(padding[3]);
                float padY = padTop + padBottom;

                // common lineHeight=49 base=40 scaleW=512 scaleH=256 pages=1 packed=0
                line = reader.readLine();
                if (line == null) throw new GdxRuntimeException("Missing common header.");
                String[] common = line.split(" ", 7); // At most we want the 6th element; i.e. "page=N"

                // At least lineHeight and base are required.
                if (common.length < 3) throw new GdxRuntimeException("Invalid common header.");

                if (!common[1].startsWith("lineHeight=")) throw new GdxRuntimeException("Missing: lineHeight");
                lineHeight = Integer.parseInt(common[1].substring(11));

                if (!common[2].startsWith("base=")) throw new GdxRuntimeException("Missing: base");
                float baseLine = Integer.parseInt(common[2].substring(5));

                // common lineHeight=49 base=40 scaleW=512 scaleH=256 pages=1 packed=0
                int pageCount = 1;
                if (common.length >= 6 && common[5] != null && common[5].startsWith("pages=")) {
                    try { pageCount = Math.max(1, Integer.parseInt(common[5].substring(6)));
                    } catch (NumberFormatException ignored) {} // Use one page.
                }

                imagePaths = new String[pageCount];

                // Read each page definition.
                // page id=0 file="verdana39distancefield.png"
                for (int p = 0; p < pageCount; p++) {
                    // page id=0 file="verdana39distancefield.png"
                    line = reader.readLine();
                    if (line == null) throw new GdxRuntimeException("Missing font page image.");
                    String[] pageLine = line.split(" ", 4);
                    if (!pageLine[2].startsWith("file=")) throw new GdxRuntimeException("Missing: page/file");

                    // Expect ID to mean "index".
                    if (pageLine[1].startsWith("id=")) {
                        try {
                            int pageID = Integer.parseInt(pageLine[1].substring(3));
                            if (pageID != p)
                                throw new GdxRuntimeException("Page IDs must be starting at 0, increasing and continues: "
                                        + pageLine[1].substring(3));
                        } catch (NumberFormatException ex) {
                            throw new GdxRuntimeException("Invalid page id: " + pageLine[1].substring(3), ex);
                        }
                    }

                    String fileName = null;
                    if (pageLine[2].endsWith("\""))
                        fileName = pageLine[2].substring(6, pageLine[2].length() - 1);
                    else fileName = pageLine[2].substring(5, pageLine[2].length());

                    imagePaths[p] = fontFile.parent().child(fileName).path().replaceAll("\\\\", "/");
                }
                descent = 0;
            
                regions = parseRegions(imagePaths); // load images as regions

                // skiped: chars count=95
                // iterate over: char id=32 x=0 y=0 width=0 height=0 xoffset=0 yoffset=40 advance=14 page=0 chnl=0
                while (true) {
                    line = reader.readLine();
                    if (line == null) break; // EOF
                    if (line.startsWith("kernings ")) break; // Starting kernings block.
                    if (!line.startsWith("char ")) continue;

                    GlyphLib.Glyph glyph = new GlyphLib.Glyph();

                    StringTokenizer tokens = new StringTokenizer(line, " =");
                    tokens.nextToken();
                    tokens.nextToken();
                    int ch = Integer.parseInt(tokens.nextToken());
                    if (ch <= 0)
                        missingGlyph = glyph;
                    else if (ch <= Character.MAX_VALUE)
                        setGlyph(ch, glyph);
                    else continue;

                    glyph.id = ch;
                    tokens.nextToken();
	                glyph.srcX = Integer.parseInt(tokens.nextToken());
	                tokens.nextToken();
	                glyph.srcY = Integer.parseInt(tokens.nextToken());
	                tokens.nextToken();
	                glyph.width = Integer.parseInt(tokens.nextToken());
	                tokens.nextToken();
	                glyph.height = Integer.parseInt(tokens.nextToken());
	                tokens.nextToken();
	                glyph.xoffset = Integer.parseInt(tokens.nextToken());
	                tokens.nextToken();
	                if (flip)
	                    glyph.yoffset = Integer.parseInt(tokens.nextToken());
	                else
	                    glyph.yoffset = -(glyph.height + Integer.parseInt(tokens.nextToken()));
	                tokens.nextToken();
	                glyph.xadvance = Integer.parseInt(tokens.nextToken());

	                // Check for page safely, it could be omitted or invalid.
	                if (tokens.hasMoreTokens()) tokens.nextToken();
	                if (tokens.hasMoreTokens()) {
	                    try {
	                        glyph.page = Integer.parseInt(tokens.nextToken());
	                    } catch (NumberFormatException ignored) { }
	                }
	                else glyph.page = 0;
	                glyph.setRegion(regions[glyph.page], flip);

                    if (glyph.width > 0 && glyph.height > 0) descent = Math.min(baseLine + glyph.yoffset, descent);
                }
                descent += padBottom;

                // kerning ...
	            while (true) {
	                line = reader.readLine();
	                if (line == null) break;
	                if (!line.startsWith("kerning ")) break;

	                /* ignore kerning (narrowing distance between W and M, WM)in v0.1
	                StringTokenizer tokens = new StringTokenizer(line, " =");
	                tokens.nextToken();
	                tokens.nextToken();
	                int first = Integer.parseInt(tokens.nextToken());
	                tokens.nextToken();
	                int second = Integer.parseInt(tokens.nextToken());
	                if (first < 0 || first > Character.MAX_VALUE || second < 0 || second > Character.MAX_VALUE) continue;
	                BitmapFont.Glyph glyph = getGlyph((char)first);
	                tokens.nextToken();
	                int amount = Integer.parseInt(tokens.nextToken());
	                if (glyph != null) { // Kernings may exist for glyph pairs not contained in the font.
	                    glyph.setKerning(second, amount);
	                }*/
	            }

	            Glyph spaceGlyph = getGlyph(' ');
	            if (spaceGlyph == null) {
	                spaceGlyph = new Glyph();
	                spaceGlyph.id = (int)' ';
	                Glyph xadvanceGlyph = getGlyph('l');
	                if (xadvanceGlyph == null) xadvanceGlyph = getFirstGlyph();
	                spaceGlyph.xadvance = xadvanceGlyph.xadvance;
	                setGlyph(' ', spaceGlyph);
	            }
	            if (spaceGlyph.width == 0) {
	                spaceGlyph.width = (int)(padLeft + spaceGlyph.xadvance + padRight);
	                spaceGlyph.xoffset = (int)-padLeft;
	            }
	            spaceWidth = spaceGlyph.width;

	            Glyph xGlyph = null;
	            for (char xChar : xChars) {
	                xGlyph = getGlyph(xChar);
	                if (xGlyph != null) break;
	            }
	            if (xGlyph == null) xGlyph = getFirstGlyph();
	            xHeight = xGlyph.height - padY;

	            Glyph capGlyph = null;
	            for (char capChar : capChars) {
	                capGlyph = getGlyph(capChar);
	                if (capGlyph != null) break;
	            }
	            if (capGlyph == null) {
	                for (Glyph[] page : this.glyphs) {
	                    if (page == null) continue;
	                    for (Glyph glyph : page) {
	                        if (glyph == null || glyph.height == 0 || glyph.width == 0) continue;
	                        capHeight = Math.max(capHeight, glyph.height);
	                    }
	                }
	            } else
	                capHeight = capGlyph.height;
	            capHeight -= padY;

	            ascent = baseLine - capHeight;
	            down = -lineHeight;
	            if (flip) {
	                ascent = -ascent;
	                down = -down;
	            }
            } catch (Exception ex) {
                ex.printStackTrace();
                throw new GdxRuntimeException(ex.getMessage());
            } finally {
                StreamUtils.closeQuietly(reader);
            }
        }

        /**Replacing snippet for loading regions in {@link BitmapFont#BitmapFont(FileHandle, FileHandle, boolean)}.<br>
         * Instead of using costume texture file path, this method are only called when parsing .fnt file (texture-file attr).
         * @param imagePathes
         * @return
        */
        private static TextureRegion[] parseRegions(String[] imagePathes) {
    	    if (imagePathes == null) return null;
		    int n = imagePathes.length;
            if (n <= 0) return new TextureRegion[0];

    	    TextureRegion[] regions = new TextureRegion[n];
		    // Load each path.
		    for (int i = 0; i < n; i++) {
			    FileHandle file = Gdx.files.internal(imagePathes[i]);
			    regions[i] = new TextureRegion(new Texture(file, false));
		    }
    	    return regions;
        }

        /**Set glyph in to {glyphs}, the glyph array.
         * @param ch
         * @param glyph
         */
        public void setGlyph (int ch, Glyph glyph) {
            if (glyphs == null)
                // FIXME This is a performance defect
                glyphs = new Glyph[PAGES][PAGE_SIZE];

			Glyph[] page = glyphs[ch / PAGE_SIZE];
			if (page == null) glyphs[ch / PAGE_SIZE] = page = new Glyph[PAGE_SIZE];
			page[ch & PAGE_SIZE - 1] = glyph;
		}

        /**Find and return the glyph(id=ch)
         * @param ch
         * @return
         */
        public Glyph getGlyph (char ch) {
			Glyph[] page = glyphs[ch / PAGE_SIZE];
			if (page != null) return page[ch & PAGE_SIZE - 1];
			return null;
		}

        /**Get any glyph not null at the first position in glyphs array.
         * @return
         */
        public Glyph getFirstGlyph () {
			for (Glyph[] page : this.glyphs) {
				if (page == null) continue;
				for (Glyph glyph : page) {
					if (glyph == null || glyph.height == 0 || glyph.width == 0) continue;
					return glyph;
				}
			}
			throw new GdxRuntimeException("No glyphs found.");
		}
    }

   	/**Represents a single character in a font page.
   	 * Replacing {@link BitmapFont.Glyph} */
	public static class Glyph {
		public int id;
		public int srcX;
		public int srcY;
		public int width, height;
		public float u, v, u2, v2;
		public int xoffset, yoffset;
		public int xadvance;
		public byte[][] kerning;
		public boolean fixedWidth;

		/** The index to the texture page that holds this glyph. */
		public int page = 0;

		public int getKerning (char ch) {
			if (kerning != null) {
				byte[] page = kerning[ch >>> LOG2_PAGE_SIZE];
				if (page != null) return page[ch & PAGE_SIZE - 1];
			}
			return 0;
		}

		public void setKerning (int ch, int value) {
			if (kerning == null) kerning = new byte[PAGES][];
			byte[] page = kerning[ch >>> LOG2_PAGE_SIZE];
			if (page == null) kerning[ch >>> LOG2_PAGE_SIZE] = page = new byte[PAGE_SIZE];
			page[ch & PAGE_SIZE - 1] = (byte)value;
		}

		public String toString () {
			return Character.toString((char)id);
		}
		
		/**Set glyph u, v.<br>
		 * Replacing {@link BitmapFont.BitmapFontData#setGlyphRegion(BitmapFont.Glyph glyph, TextureRegion region)}
		 * @param region
		 */
		public void setRegion(TextureRegion region, boolean flipped) {
			Texture texture = region.getTexture();
			float invTexWidth = 1.0f / texture.getWidth();
			float invTexHeight = 1.0f / texture.getHeight();

			float offsetX = 0, offsetY = 0;
			float u = region.getU();
			float v = region.getV();
			float regionWidth = region.getRegionWidth();
			float regionHeight = region.getRegionHeight();
			if (region instanceof AtlasRegion) {
				// Compensate for whitespace stripped from left and top edges.
				AtlasRegion atlasRegion = (AtlasRegion)region;
				offsetX = atlasRegion.offsetX;
				offsetY = atlasRegion.originalHeight - atlasRegion.packedHeight - atlasRegion.offsetY;
			}

			float x = this.srcX;
			float x2 = this.srcX + this.width;
			float y = this.srcY;
			float y2 = this.srcY + this.height;

			// Shift glyph for left and top edge stripped whitespace. Clip glyph for right and bottom edge stripped whitespace.
			if (offsetX > 0) {
				x -= offsetX;
				if (x < 0) {
					this.width += x;
					this.xoffset -= x;
					x = 0;
				}
				x2 -= offsetX;
				if (x2 > regionWidth) {
					this.width -= x2 - regionWidth;
					x2 = regionWidth;
				}
			}
			if (offsetY > 0) {
				y -= offsetY;
				if (y < 0) {
					this.height += y;
					y = 0;
				}
				y2 -= offsetY;
				if (y2 > regionHeight) {
					float amount = y2 - regionHeight;
					this.height -= amount;
					this.yoffset += amount;
					y2 = regionHeight;
				}
			}

			this.u = u + x * invTexWidth;
			this.u2 = u + x2 * invTexWidth;
			if (flipped) {
				this.v = v + y * invTexHeight;
				this.v2 = v + y2 * invTexHeight;
			} else {
				this.v2 = v + y * invTexHeight;
				this.v = v + y2 * invTexHeight;
			}
		}
	}

}
