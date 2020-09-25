package io.odysz.ext.bisheng;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.PerspectiveCamera;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g3d.Model;
import com.badlogic.gdx.graphics.g3d.Renderable;
import com.badlogic.gdx.graphics.g3d.model.NodePart;
import com.badlogic.gdx.graphics.glutils.ShaderProgram;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Vector3;

import io.odysz.ext.CamRoller;

/**Modified on 12/11/17: reserved working version, which will display a 'C' in gradient color.<br>
 * Created by ody on 5/17/17.
 */
public class TestBisheng implements ApplicationListener {
    private static final int GlyphTex0 = 0;

    /**Distance Field Font shader. */
    private static class BishengShader extends ShaderProgram {

		public BishengShader () {
			super(Gdx.files.internal("fonts/distancefield.vert"),
                  Gdx.files.internal("fonts/distancefield.frag"));
			if (!isCompiled()) {
				throw new RuntimeException("Shader compilation failed:\n" + getLog());
			}
		}

		/** @param weight a value between 0 and 1 */
		public void setUniforms (float weight) {
			float delta = 0.5f * MathUtils.clamp(weight, 0, 1);
			setUniformf("u_lower", 0.5f - delta);
			setUniformf("u_upper", 0.5f + delta);
            setUniformi("u_texture", GlyphTex0);
		}
	}

	private PerspectiveCamera camera;
	CamRoller inputProcessor;

    private SpriteBatch spriteBatch;
//	private Texture distanceFieldTexture;
	private GlyphLib glib;
	private BishengShader sdfShader;

	private Renderable renderable;
	private Vector3 center = new Vector3(2, 45, 0);

    /**Create camera, model, attatch bisheng shader;
     * Bind a string of glyph to the model.
     * */
    @Override
	public void create() {
		float w = Gdx.graphics.getWidth();
		float h = Gdx.graphics.getHeight();

		camera = new PerspectiveCamera(35f, w, h);
		camera.up.set(0, 1, 0);
		camera.position.set(0, 0, 1500);
		camera.lookAt(0, 0, 0);
		camera.near = 0.1f;
		camera.far = 40000f;

		inputProcessor = new CamRoller(camera);
		Gdx.input.setInputProcessor(inputProcessor);

        spriteBatch = new SpriteBatch();
//		distanceFieldTexture = new Texture(Gdx.files.internal("fonts/verdana39distancefield.png"), true);
		glib = new GlyphLib(Gdx.files.internal("fonts/verdana39distancefield.fnt"), false);
		Model typoModel = glib.bindFrame("C-X", Color.RED, GlyphTex0);
        typoModel.calculateTransforms();

        renderable = new Renderable();
        NodePart blockPart = typoModel.nodes.get(0).parts.get(0);
        blockPart.setRenderable(renderable);
        renderable.environment = null;
 
		sdfShader = new BishengShader();
		ShaderProgram.pedantic = false; // Useful when debugging this test
        if (!sdfShader.isCompiled())
            System.out.println(sdfShader.getLog());

        renderable.worldTransform.translate(center);
        sdfShader.bind();
        sdfShader.setUniformMatrix("modelWorld", renderable.worldTransform);

        Gdx.gl.glActiveTexture(GL20.GL_TEXTURE0);
	}

	@Override
	public void dispose() {
        spriteBatch.dispose();
        //distanceFieldTexture.dispose();
        glib.dispose();
        sdfShader.dispose();
	}

	@Override
	public void render() {
		inputProcessor.pullInputs();
        // time = TimeUtils.nanoTime();

        Gdx.gl20.glEnable(GL20.GL_BLEND);
        Gdx.gl20.glBlendFunc(GL20.GL_SRC_ALPHA, GL20.GL_ONE_MINUS_SRC_ALPHA);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT | GL20.GL_DEPTH_BUFFER_BIT);

        camera.update();

        spriteBatch.enableBlending();
        spriteBatch.begin();
//        sdfShader.bind();
//        sdfShader.setUniformMatrix("modelWorld", renderable.worldTransform);

        //spriteBatch.draw(texBase, 0, 0);
        //spriteBatch.flush();

        sdfShader.setUniforms(0.6f);
        spriteBatch.setShader(sdfShader);

        renderable.meshPart.render(sdfShader);

        spriteBatch.end();
	}

//	private Vector3 tempV3 = new Vector3();

	@Override
	public void resize(int width, int height) {
		camera.viewportWidth = width;
		camera.viewportHeight = height;
	}

	@Override
	public void pause() { }

	@Override
	public void resume() { }
}
