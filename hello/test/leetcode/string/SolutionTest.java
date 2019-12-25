package leetcode.string;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class SolutionTest {

	@Test
	void testMyAtoi() {
        Q008_atoi s = new Q008_atoi();
        assertEquals(0, s.myAtoi(" "));
        assertEquals(0, s.myAtoi(" -"));
        assertEquals(0, s.myAtoi(" +"));
        assertEquals(0, s.myAtoi("+"));
        assertEquals(0, s.myAtoi(""));
        assertEquals(0, s.myAtoi("0"));
        assertEquals(0, s.myAtoi("+0"));
        assertEquals(0, s.myAtoi("-0"));
        assertEquals(-1, s.myAtoi("-01"));
        assertEquals(42, s.myAtoi("42"));
        assertEquals(-1, s.myAtoi("-1"));
        assertEquals(1, s.myAtoi("+1"));
        assertEquals(0, s.myAtoi("+00000"));
        assertEquals(20, s.myAtoi("+0000020"));
        assertEquals(-20, s.myAtoi("-0000020"));
        assertEquals(0, s.myAtoi("----0000020"));
        assertEquals(0, s.myAtoi("+-2"));
        assertEquals(0, s.myAtoi("+++-2"));
        assertEquals(0, s.myAtoi("-++-2"));
        assertEquals(0, s.myAtoi("-+++2"));
        assertEquals(0, s.myAtoi("-++ 2"));
        assertEquals(-2, s.myAtoi("-2 ++ 4"));
        assertEquals(0, s.myAtoi("--2"));
        assertEquals(0, s.myAtoi(" + + 2 2 0"));
        assertEquals(0, s.myAtoi("+.2 2 0"));
        assertEquals(-2, s.myAtoi(" -2 ++ 3"));
        assertEquals(0, s.myAtoi("- 2 ++ 3"));
        assertEquals(0, s.myAtoi("-00000"));
        assertEquals(0, s.myAtoi("0"));
        assertEquals(-42, s.myAtoi("-42"));
        assertEquals(0, s.myAtoi("words and 987"));
        assertEquals(4193, s.myAtoi("4193 with words"));
        assertEquals(4193, s.myAtoi("4193-with-words"));
        assertEquals(419, s.myAtoi("+419-3-with-words"));
        assertEquals(41, s.myAtoi("41-9+3-with-words"));
        assertEquals(41, s.myAtoi("+41-9+3-with-words"));
        assertEquals(-4193, s.myAtoi("-4193 "));
        assertEquals(0x3FFFFFFF , s.myAtoi(" 1073741823 "));
        assertEquals(0x40000000 , s.myAtoi(" 1073741824 "));
        assertEquals(0x40000001 , s.myAtoi(" 1073741825 "));
        assertEquals(0x40000002 , s.myAtoi(" 1073741826 "));
        assertEquals(-1073741823 , s.myAtoi("-1073741823 "));
        assertEquals(-1073741824 , s.myAtoi("-1073741824 "));
        assertEquals(-1073741825 , s.myAtoi("-1073741825 "));
        assertEquals(0x7FFFFFFE , s.myAtoi(" 2147483646 "));
        assertEquals(0x7FFFFFFF , s.myAtoi(" 2147483647 "));
        assertEquals(0x7FFFFFFF , s.myAtoi(" 2147483648 "));
        assertEquals(0x80000001, s.myAtoi(" -2147483647 "));
        assertEquals(0x80000000, s.myAtoi(" -2147483648 "));
        assertEquals(0x80000000, s.myAtoi(" -2147483649 "));
        assertEquals(0x80000000, s.myAtoi(" -4294967296 "));
        assertEquals(0x7FFFFFFF, s.myAtoi(" 4294967295 "));
        //             1852516352            2147483648
        assertEquals(0x80000000, s.myAtoi(" -2147483649 "));
        assertEquals(0x80000000, s.myAtoi(" -2347483648 "));
        assertEquals(0x80000000, s.myAtoi(" -2447483648 "));
        assertEquals(0x80000000, s.myAtoi(" -2847483648 "));
        assertEquals(0x80000000, s.myAtoi(" -3147483648 "));
        assertEquals(0x80000000, s.myAtoi(" -4147483648 "));
        assertEquals(0x80000000, s.myAtoi("-6147483648"));
        assertEquals(-2147483648, s.myAtoi("-91283472332"));
	}

}
