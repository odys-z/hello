package io.odysz.g.hello;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.PerspectiveCamera;
import com.badlogic.gdx.graphics.Pixmap;
import com.badlogic.gdx.graphics.g2d.BitmapFont;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.glutils.ShaderProgram;
import com.badlogic.gdx.math.Vector3;

import io.odysz.ext.CamRoller;
import io.odysz.ext.Skybox;
import io.odysz.ext.SkyboxShader;

/**
 * Created by ody on 5/17/17.
 */
public class Fresnels implements ApplicationListener {
	private PerspectiveCamera camera;

	CamRoller inputProcessor;

	private ShaderProgram skyboxShader;
//	private ShaderProgram waterShader;

	// private WaterFBO waterFbo;

	private Pixmap[] texturesSkyBox;
	private Skybox skybox;

	// private float time;
	//private FresnelMesh fresnel;
	private FresnelMesh fresnel;

	@Override
	public void create() {
		float w = Gdx.graphics.getWidth();
		float h = Gdx.graphics.getHeight();

		camera = new PerspectiveCamera(35f, w, h);
		camera.up.set(0, 1, 0);
		camera.position.set(0, 0, 1500);
		camera.lookAt(0, 0, 0);
		camera.near = 0.1f;
		camera.far = -40000f;

		skyboxShader = new ShaderProgram(SkyboxShader.vertexShader,
				SkyboxShader.fragmentShader);
		if (skyboxShader.isCompiled() == false) {
			throw new RuntimeException("Could not load skybox shader: "
					+ skyboxShader.getLog());
		}

//		waterShader = new ShaderProgram(WaterShader.vertexShader,
//				WaterShader.fragmentShader);
//		if (waterShader.isCompiled() == false) {
//			throw new RuntimeException("Could not load water shader: "
//					+ waterShader.getLog());
//		}

		texturesSkyBox = new Pixmap[6];
        // enum Format {Alpha, Intensity, LuminanceAlpha, RGB565, RGBA4444, RGB888, RGBA8888};
        // int alpha = Pixmap.Format.Alpha.ordinal(); -- alpha = 0

		// Image source: http://www.codemonsters.de/home/content.php?show=cubemaps
		texturesSkyBox[0] = new Pixmap( // right
				Gdx.files.internal("textures/brightday1_positive_x565_2.png"));
		texturesSkyBox[1] = new Pixmap( // left
				Gdx.files.internal("textures/brightday1_negative_x.png"));
		texturesSkyBox[2] = new Pixmap( // top
				Gdx.files.internal("textures/brightday1_positive_y.png"));
		texturesSkyBox[3] = new Pixmap( // down
				Gdx.files.internal("textures/brightday1_negative_y.png"));
		texturesSkyBox[4] = new Pixmap( // front
				Gdx.files.internal("textures/brightday1_positive_z.png"));
		texturesSkyBox[5] = new Pixmap( // back
				Gdx.files.internal("textures/brightday1_negative_z565.png"));

		skybox = new Skybox(texturesSkyBox);

//		waterFbo = new WaterFBO(skybox.getCubeMapTextureUnit());
        //water = new Water3(skybox.getCubeMapTextureUnit());

		inputProcessor = new CamRoller(camera);
		Gdx.input.setInputProcessor(inputProcessor);

		fresnel = new FresnelMesh(camera, skybox.getCubeMapTextureUnit(), new Vector3(0, 0, 0), new Vector3(500, 500, 500));

		//font = new BitmapFont(Gdx.files.internal("assets/font.fnt"), Gdx.files.internal("assets/font.png"), false);
		font = new BitmapFont();
		font.getData().setScale(1.5f, 1.5f);
		batcher = new SpriteBatch();
	}

	@Override
	public void dispose() {
		for (Pixmap texture : texturesSkyBox) {
			texture.dispose();
		}
		if (skybox != null) skybox.dispose();
//		if (waterFbo != null) waterFbo.dispose();
		if (fresnel != null) fresnel.dispose();
	}

	@Override
	public void render() {
		inputProcessor.pullInputs();

        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT | GL20.GL_DEPTH_BUFFER_BIT);
        Gdx.gl.glDisable(GL20.GL_CULL_FACE);
        Gdx.gl.glEnable(GL20.GL_DEPTH_TEST);
        Gdx.gl.glEnable(GL20.GL_BLEND);
        // glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
        Gdx.gl.glBlendFunc(GL20.GL_SRC_ALPHA, GL20.GL_ONE_MINUS_SRC_ALPHA);

		camera.update();

		skyboxShader.bind();
		skybox.render(skyboxShader, camera);

        /*
		time += Gdx.graphics.getDeltaTime();
		waterShader.begin();
		waterFbo.render(waterShader, camera, time);
        waterShader.end();
        */

		if (fresnel != null) fresnel.render();
		else System.out.println("-------------------");

		renderFPS();
	}

	// private Vector3 tempV3 = new Vector3();

	private BitmapFont font;
	public SpriteBatch batcher;
	private void renderFPS() {
		//batcher.setProjectionMatrix(camera.combined);
		batcher.begin();
		font.draw(batcher, String.format("FPS: %s", Gdx.graphics.getFramesPerSecond()), 100, 400);
//        font.draw(batcher, String.format("Camera Pos: %6.2f, %6.2f, %6.2f", camera.position.x, camera.position.y, camera.position.z), 100, 344);
//        font.draw(batcher, String.format("temple Pos: %6.2f, %6.2f, %6.2f", fresnel.tempos.x, fresnel.tempos.y, fresnel.tempos.z), 100, 322);
//        fresnel.renderable.worldTransform.getTranslation(tempV3);
//        font.draw(batcher, String.format("translate : %6.2f, %6.2f, %6.2f", tempV3.x, tempV3.y, tempV3.z), 100, 300);
		batcher.end();
	}

	@Override
	public void resize(int width, int height) {
		camera.viewportWidth = width;
		camera.viewportHeight = height;
//		if (waterFbo != null) waterFbo.resize(width, height);
	}

	@Override
	public void pause() { }

	@Override
	public void resume() { }
}
