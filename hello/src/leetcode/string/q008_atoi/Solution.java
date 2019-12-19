package leetcode.string.q008_atoi;

/**
 * 8. String to Integer (atoi)
 * https://leetcode.com/problems/string-to-integer-atoi/
 * 
 * Runtime: 1 ms, faster than 100.00% of Java online submissions for String to Integer (atoi).<br>
 * Memory Usage: 35.9 MB, less than 100.00% of Java online submissions for String to Integer (atoi).
 * @author odys-z@github.com
 *
 */
public class Solution {
    public int myAtoi(String str) {
    	if (str == null)
    		return 0;
    	int l = str.length();
    	if (l == 0)
    		return 0;
    	
    	int sign = 0;
    	int sum = 0;
    	
    	for (int i = 0; i < l; i++) {
    		if (sign == 0) {
    			char c = str.charAt(i);
    			while (c == ' ') {
    				i++;
    				if (i >= l)
    					return 0;
    				c = str.charAt(i);
    			}
				if ('+' == c) {
					sign = 1;
					continue;
				}
				else if (c == '-') {
					sign = -1;
					continue;
				}
    		}

    		char c = str.charAt(i);
    		if (c < '0' || c > '9')
    			return sum * sign;
    		else if (sign == 0)
				sign = 1;

			int sum2 = sum << 1;
			int sum8 = sum2 << 2;
			
			if (sum > 0x10000000 || sum2 < 0 || sum2 > 0x20000000 || sum8 < 0)
				return sign > 0 ? 0x7FFFFFFF : 0x80000000;
			else
				sum = sum2 + sum8 + (c - '0');

			if (sum < 0)
				return sign > 0 ? 0x7FFFFFFF : 0x80000000;
    	}
    	
    	return sign * sum;
    }
}