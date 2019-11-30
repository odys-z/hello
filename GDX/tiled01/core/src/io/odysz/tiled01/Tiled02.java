package io.odysz.tiled01;

import com.badlogic.gdx.ApplicationAdapter;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.GL20;
import com.badlogic.gdx.graphics.OrthographicCamera;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureAtlas;
import com.badlogic.gdx.maps.tiled.TiledMap;
import com.badlogic.gdx.maps.tiled.TiledMapRenderer;
import com.badlogic.gdx.maps.tiled.TmxMapLoader;
import com.badlogic.gdx.maps.tiled.renderers.OrthogonalTiledMapRenderer;
import com.badlogic.gdx.math.Vector2;
import com.badlogic.gdx.physics.box2d.Box2D;
import com.badlogic.gdx.physics.box2d.World;

public class Tiled02 extends ApplicationAdapter implements InputProcessor {
	SpriteBatch batch;
	Texture oz;
	TiledMap tiledMap;
	OrthographicCamera camera;
	TiledMapRenderer tiledMapRenderer;

	float w, h;
	int ozw, ozh;
	int dx = 0;
	int dy = 0;
	boolean keypress = false;

	private TextureAtlas textureAtlas;
	private World world;

	@Override
	public void create () {
		Box2D.init();
		world = new World(new Vector2(0, -10), true);

		w = Gdx.graphics.getWidth();
		h = Gdx.graphics.getHeight();

		batch = new SpriteBatch();
		oz = new Texture("oz.png");
		ozw = oz.getWidth();
		ozh = oz.getHeight();

		camera = new OrthographicCamera();
		camera.setToOrtho(false,w,h);
		camera.update();
		tiledMap = new TmxMapLoader().load("w32h32.tmx");
		tiledMapRenderer = new OrthogonalTiledMapRenderer(tiledMap);


		textureAtlas = new TextureAtlas("sprites.txt");
		Sprite sprite = textureAtlas.createSprite("banana");

		Gdx.input.setInputProcessor(this);
	}

	@Override
	public void render () {
		Gdx.gl.glBlendFunc(GL20.GL_SRC_ALPHA, GL20.GL_ONE_MINUS_SRC_ALPHA);
		Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
		if (keypress)
			camera.translate(dx, dy);
		camera.update();


		tiledMapRenderer.setView(camera);
		tiledMapRenderer.render();

		batch.begin();
		batch.draw(oz, w / 2 - ozw, w / 2 - ozh);
		batch.end();
	}

	@Override
	public boolean keyDown(int keycode) {
		if(keycode == Input.Keys.LEFT)
			dx = 1;
		if(keycode == Input.Keys.RIGHT)
			dx = -1;
		if(keycode == Input.Keys.UP)
			dy = 1;
		if(keycode == Input.Keys.DOWN)
			dy = -1;

		if(keycode == Input.Keys.NUM_1)
			tiledMap.getLayers().get(0).setVisible(!tiledMap.getLayers().get(0).isVisible());
		if(keycode == Input.Keys.NUM_2)
			tiledMap.getLayers().get(1).setVisible(!tiledMap.getLayers().get(1).isVisible());

		keypress = true;
		return false;
	}

	@Override
	public boolean keyUp(int keycode) {
//		if(keycode == Input.Keys.LEFT)
//			camera.translate(-32,0);
//		if(keycode == Input.Keys.RIGHT)
//			camera.translate(32,0);
//		if(keycode == Input.Keys.UP)
//			camera.translate(0,+32);
//		if(keycode == Input.Keys.DOWN)
//			camera.translate(0,-32);
//		if(keycode == Input.Keys.NUM_1)
//			tiledMap.getLayers().get(0).setVisible(!tiledMap.getLayers().get(0).isVisible());
//		if(keycode == Input.Keys.NUM_2)
//			tiledMap.getLayers().get(1).setVisible(!tiledMap.getLayers().get(1).isVisible());
		keypress = false;
		return false;
	}

	@Override
	public boolean keyTyped(char character) {
		return false;
	}

	@Override
	public boolean touchDown(int screenX, int screenY, int pointer, int button) {
		return false;
	}

	@Override
	public boolean touchUp(int screenX, int screenY, int pointer, int button) {
		return false;
	}

	@Override
	public boolean touchDragged(int screenX, int screenY, int pointer) {
		return false;
	}

	@Override
	public boolean mouseMoved(int screenX, int screenY) {
		return false;
	}

	@Override
	public boolean scrolled(int amount) {
		return false;
	}

	@Override
	public void dispose () {
		batch.dispose();
		oz.dispose();
		world.dispose();
	}
}
