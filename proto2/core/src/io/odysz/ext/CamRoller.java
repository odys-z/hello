package io.odysz.ext;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input.Keys;
import com.badlogic.gdx.InputProcessor;
import com.badlogic.gdx.graphics.Camera;
import com.badlogic.gdx.math.Matrix4;
import com.badlogic.gdx.math.Vector3;

public class CamRoller implements InputProcessor {

	// ===========================================================
	// Constants
	// ===========================================================

	private final static float COEFF_DELTA = 0.01f;
	private final static float COEFF_TRANSLATION = 3f;

	// ===========================================================
	// Fields
	// ===========================================================

	private Camera camera;
	private int lastScreenX;
	private int lastScreenY;

	private Matrix4 temp;
	private Vector3 rotateAxis;
	private Matrix4 tempPull;
	private Vector3 direction;

	// ===========================================================
	// Constructors
	// ===========================================================

	public CamRoller(Camera camera) {
		this.camera = camera;
		lastScreenX = 0;
		lastScreenY = 0;

		temp = new Matrix4();
		rotateAxis = new Vector3();
		tempPull = new Matrix4();
		direction = new Vector3();
	}

	// ===========================================================
	// Getter & Setter
	// ===========================================================

	// ===========================================================
	// Methods for/from SuperClass/Interfaces
	// ===========================================================

	@Override
	public boolean keyDown(int keycode) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean keyUp(int keycode) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean keyTyped(char character) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean touchDown(int screenX, int screenY, int pointer, int button) {
		lastScreenX = screenX;
		lastScreenY = screenY;
		return true;
	}

	@Override
	public boolean touchUp(int screenX, int screenY, int pointer, int button) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean touchDragged(int screenX, int screenY, int pointer) {
		float deltaX = screenX - lastScreenX;
		float deltaY = -(screenY - lastScreenY);

		// delta X rotates around scree up
		temp.idt();
		temp.rotate(camera.up, COEFF_DELTA * deltaX);
		// delta Y rotates camera.x
		rotateAxis.set(camera.direction);
		rotateAxis.crs(camera.up);
		temp.rotate(rotateAxis, COEFF_DELTA * deltaY);
		// rotate !
		camera.direction.mul(temp).nor();
        /**
		System.out.println("-- -- -- -- -- -- -- -- -- -- ");
		System.out.println(String.format("x = %6f, y = %6f", deltaX, deltaY));
		System.out.println(camera.combined);
         */

		camera.update();
		return true;
	}

	@Override
	public boolean mouseMoved(int screenX, int screenY) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean scrolled(int amount) {
		// TODO Auto-generated method stub
		return false;
	}

	// ===========================================================
	// Methods
	// ===========================================================

	public void pullInputs() {
		if (Gdx.input.isKeyPressed(Keys.UP)) {
			Vector3 direction = getDirectionZNull();
			tempPull.idt().translate(direction);
			camera.position.mul(tempPull);
		} else if (Gdx.input.isKeyPressed(Keys.DOWN)) {
			// Vector3 direction = getDirectionZNull().mul(-1).nor();
			Vector3 direction = getDirectionZNull().scl(-1).nor();
			tempPull.idt().translate(direction);
			camera.position.mul(tempPull);
		}

		if (Gdx.input.isKeyPressed(Keys.LEFT)) {
			// Vector3 direction = getDirectionZNull().crs(0, 0, 1).nor().mul(-COEFF_TRANSLATION);
			Vector3 direction = getDirectionZNull().crs(0, 0, 1).nor().scl(-COEFF_TRANSLATION);
			tempPull.idt().translate(direction);
			camera.position.mul(tempPull);
		} else if (Gdx.input.isKeyPressed(Keys.RIGHT)) {
			// Vector3 direction = getDirectionZNull().crs(0, 0, 1).nor().mul(COEFF_TRANSLATION);
			Vector3 direction = getDirectionZNull().crs(0, 0, 1).nor().scl(COEFF_TRANSLATION);
			tempPull.idt().translate(direction);
			camera.position.mul(tempPull);
		}
		
	}
	
	private Vector3 getDirectionZNull(){
		direction.set(camera.direction);
		direction.set(direction.x, direction.y, 0).nor();
		// direction.mul(COEFF_TRANSLATION);
		direction.scl(COEFF_TRANSLATION);
		return direction;
	}

	// ===========================================================
	// Inner and Anonymous Classes
	// ===========================================================
}
