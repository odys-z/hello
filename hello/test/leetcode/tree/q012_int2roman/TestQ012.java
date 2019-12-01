package leetcode.tree.q012_int2roman;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * 12. Integer to Roman
 * https://leetcode.com/problems/integer-to-roman/
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

 * @author odys-z@github.com
 *
 */
class TestQ012 {

	private Solution s;

	@BeforeEach
	void setUp() throws Exception {
//		s = new Solution();
//		s = new SolutionRef();
		s = new SolutionRanktable();
	}

	@Test
	void test() {
        assertEquals("I", s.intToRoman(1));
        assertEquals("III", s.intToRoman(3));
        assertEquals("IV", s.intToRoman(4));
        assertEquals("V", s.intToRoman(5));
        assertEquals("VI", s.intToRoman(6));
        assertEquals("IX", s.intToRoman(9));
        assertEquals("X", s.intToRoman(10));
        assertEquals("XI", s.intToRoman(11));
        assertEquals("XIV", s.intToRoman(14));
        assertEquals("XV", s.intToRoman(15));
        assertEquals("XVI", s.intToRoman(16));
        assertEquals("XIX", s.intToRoman(19));
        assertEquals("XX", s.intToRoman(20));
        assertEquals("XXIV", s.intToRoman(24));
        assertEquals("XXXIX", s.intToRoman(39));
        assertEquals("LVIII", s.intToRoman(58));
        assertEquals("XCIX", s.intToRoman(99));
        assertEquals("C", s.intToRoman(100));
        assertEquals("CI", s.intToRoman(101));
        assertEquals("CCI", s.intToRoman(201));
        assertEquals("CD", s.intToRoman(400));
        assertEquals("CDI", s.intToRoman(401));
        assertEquals("DCCCLXXVI", s.intToRoman(876));
        assertEquals("CMLXXXVII", s.intToRoman(987));
        assertEquals("MMMCDXXXII", s.intToRoman(3432));
        assertEquals("MMMCDXXXIX", s.intToRoman(3439));
        assertEquals("MMMCDXCIX", s.intToRoman(3499));
        assertEquals("M", s.intToRoman(1000));
        assertEquals("MI", s.intToRoman(1001));
        assertEquals("MCMXCIV", s.intToRoman(1994));
	}

}
