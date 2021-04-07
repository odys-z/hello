package leetcode.string;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;


class Q004Test {
	private Q004_palindrom s;

	@BeforeEach
	void setUp() throws Exception {
//		s = new Solution();
//		s = new SolutionRef();
		s = new Q004_palindrom();
	}


	@Test
	void testLongestPalindrome() {
        assertEquals("a", s.longestPalindrome("a"));
        assertEquals("a", s.longestPalindrome("ab"));
        assertEquals("bb", s.longestPalindrome("bb"));
        assertEquals("a", s.longestPalindrome("abc"));
        assertEquals("a", s.longestPalindrome("abcd"));
        assertEquals("", s.longestPalindrome(""));
        assertEquals("aba", s.longestPalindrome("aba"));
        assertEquals("bab", s.longestPalindrome("babad"));
        assertEquals("babab", s.longestPalindrome("bababd"));
        assertEquals("bab", s.longestPalindrome("babad"));
        assertEquals("adada", s.longestPalindrome("babadada"));
        assertEquals("cccccc fdfdfebbbbbbbbbbefdfdf cccccc",
                         s.longestPalindrome("babadbbcdfavvedf feescsefcv   svsvscxseretv dfhbdsvfdgbhyn  bbrdherrvgerg  svsgr54yurrtjk6fgfbfhtgsgtcccccc fdfdfebbbbbbbbbbefdfdf ccccccdededde"));
	}

}
