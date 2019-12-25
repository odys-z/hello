package leetcode.tree;


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

class Q012_int2roman {
    public String intToRoman(int num) {
    	StringBuffer sb = new StringBuffer();
    	maxr = strs.length - 1;
    	while (num > 0) {
    		int ix = bins(num, 0, Math.min(maxr, nums.length - 1)); 
    		while (num >= nums[ix]) {
    			num -= nums[ix];
    			sb.append(strs[ix]);
    		}
    	}
    	return sb.toString();
    }

    static int[] nums =    new int[]    { 1,   4,    5,   9,    10,  40,   50,  90,   100, 400,  500, 900,  1000};
	static String[] strs = new String[] {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
    static int maxr = strs.length - 1;

    public static int bins(int looking, int l, int r) {
    	if (looking == nums[r])
    		return r;
    	else if (looking == nums[l])
    		return l;
    	if (l == r)
    		return l;

    	int m = (r + l) / 2;
    	
    	if (looking >= nums[m] && looking < nums[m + 1])
    		return m;
    	else if (looking < nums[m]) {
    		maxr = Math.min(m - 1, maxr);
    		return bins(looking, l, m - 1);
    	}
    	else return bins(looking, m + 1, r);
    }
}
