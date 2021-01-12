package leetcode.regex;

//import static org.junit.jupiter.api.Assertions.*;

import org.junit.Assert;
import org.junit.jupiter.api.Test;

class Q010Test {

	@Test
	void test() {
		Q010 parser = new Q010(); 
		Assert.assertTrue(parser.isMatch(null, null));
		Assert.assertTrue(parser.isMatch("", null));
		Assert.assertTrue(parser.isMatch("", ""));
		Assert.assertTrue(parser.isMatch("", ".*"));
		Assert.assertTrue(parser.isMatch(null, ".*"));
		Assert.assertFalse(parser.isMatch("", "a"));
		Assert.assertTrue(parser.isMatch("", "a*"));
		Assert.assertTrue(parser.isMatch("", "c*c*"));
//		Assert.assertFalse(parser.isMatch1("", "c**"));
//		Assert.assertFalse(parser.isMatch("", "c**"));
		Assert.assertFalse(parser.isMatch("a", ""));
		Assert.assertTrue(parser.isMatch("a", "a"));
		Assert.assertFalse(parser.isMatch("aa", "a"));
		Assert.assertTrue(parser.isMatch("ab", ".b"));
		Assert.assertTrue(parser.isMatch("ab", ".*"));
		Assert.assertTrue(parser.isMatch("aaa", ".*"));
		Assert.assertTrue(parser.isMatch("aab", "c*a*b"));
		Assert.assertFalse(parser.isMatch("mississippi", "mis*is*p*."));

		Assert.assertTrue(parser.isMatch("mississippi", "mis*is*ip*."));
		Assert.assertTrue(parser.isMatch("mississi", "mis*is*i*"));
		Assert.assertFalse(parser.isMatch("mississi", "mis*is*i."));
		Assert.assertTrue(parser.isMatch("mississi", "mis*is*i.*"));
		Assert.assertTrue(parser.isMatch("mississi", "mis*is*i"));
		Assert.assertTrue(parser.isMatch("{\"\":\"ississ123}", "{\"\":\"is*is*123}"));
		Assert.assertTrue(parser.isMatch("{\"\":  123}", "{\"\": *123}"));
		Assert.assertTrue(parser.isMatch("mississi", "...*is*i"));
		Assert.assertTrue(parser.isMatch("mississi", ".*i.*i.*i.*"));
		Assert.assertTrue(parser.isMatch("iii", ".*i.*i.*i.*"));
		Assert.assertTrue(parser.isMatch("1i2ii4", ".*i.*i.*i.*"));
		Assert.assertTrue(parser.isMatch("1i2i i", ".*i.*i.*i.*"));
		Assert.assertTrue(parser.isMatch("i i iss", ".*i.*i.*i.*"));
		Assert.assertFalse(parser.isMatch("i", ".*i.*i"));
	}

}
