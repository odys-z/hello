package io.oz.hello.gltf.desktop;

import com.badlogic.gdx.backends.lwjgl.LwjglApplication;
import com.badlogic.gdx.backends.lwjgl.LwjglApplicationConfiguration;
import io.oz.hello.gltf.Scene1;
import net.mgsx.gltf.demo.GLTFDemo;

public class DesktopLauncher {
	public static void main (String[] arg) {
		LwjglApplicationConfiguration config = new LwjglApplicationConfiguration();
//		new LwjglApplication(new Scene1(), config);
		new LwjglApplication(new GLTFDemo(), config);
	}
}
