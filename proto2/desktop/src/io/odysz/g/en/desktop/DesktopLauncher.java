package io.odysz.g.en.desktop;

import com.badlogic.gdx.backends.lwjgl.LwjglApplication;
import com.badlogic.gdx.backends.lwjgl.LwjglApplicationConfiguration;

import io.odysz.ext.bisheng.TestBisheng;
import io.odysz.g.en.SceneB2;
import io.odysz.g.hello.Fresnels;

/**Use eclilpse to debug. 
 * see <a href='https://stackoverflow.com/questions/56305318/could-not-find-or-load-main-class-with-intellij-application-configuration'>
 * Could not find or load main class with IntelliJ Application configuration</a> and
 * <a href='https://youtrack.jetbrains.com/issue/IDEA-122904'>AS Issue</a>
 * 
 * @author odys-z@github.com
 *
 */
public class DesktopLauncher {
	public static void main (String[] arg) {
		LwjglApplicationConfiguration config = new LwjglApplicationConfiguration();
		// new LwjglApplication(new SceneB2(), config); // works
//		 new LwjglApplication(new Fresnels(), config); // works
		new LwjglApplication(new TestBisheng(), config);
	}
}
