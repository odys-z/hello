package io.oz.hello;


import static org.junit.jupiter.api.Assertions.fail;

import java.io.File;

import org.junit.Test;

import io.odysz.common.Utils;

public class FFProbeWrapperTest {

	@Test
	public void testParseAttributes() throws Exception {
		
		FFProbeWrapper.parseAttributes("resources/1.mp4");
		// fail("Not yet implemented");
	}

}
