/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package io.odysz.hello.gradle.java;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    @Test void appHasAGreeting() {
        App classUnderTest = new App();
        assertNotNull(classUnderTest.getGreeting(), "app should have a greeting");
        assertEquals(classUnderTest.getPackage(), "io.odysz.hello", "f2");
    }
}