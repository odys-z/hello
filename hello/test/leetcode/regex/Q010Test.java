package leetcode.regex;

//import static org.junit.jupiter.api.Assertions.*;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

class Q010Test {

	@Test
	void test() {
		Q010 parser = new Q010(); 
		Assert.assertTrue(parser.isMatch("a", "a"));
		Assert.assertFalse(parser.isMatch("aa", "a"));
		Assert.assertTrue(parser.isMatch("ab", ".b"));
		Assert.assertTrue(parser.isMatch("aaa", ".*"));
		Assert.assertFalse(parser.isMatch("", "a"));
		Assert.assertTrue(parser.isMatch("", null));
	}

}
