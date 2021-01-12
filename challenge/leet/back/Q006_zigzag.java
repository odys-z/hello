package leetcode.array;

/**
 * 6. ZigZag Conversion
 * https://leetcode.com/problems/zigzag-conversion/
 * 
 * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
 * (you may want to display this pattern in a fixed font for better legibility) <pre>
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
</pre>
 *
 * @author odys-z@github.com
 */
public class Q006_zigzag {

    /**<pre>
		v = 0	v = 1 			v = 2			v = 3
u = 0	0		 [ ]			2(k-1)			[ ]					4(k-1)
u = 1	1		k-1 + k-2		2(k-1) + 1		3(k-1) + k-2 
u = 2	2		k-1 + k-3
	
u = k-2	k-2		k-1 + 1			2(k-1) + k-2	3(k-1) + 1
u = k-1	[ ]		k-1 + 0			[ ]				3(k-1) + 0

     where
     Z[0, 0] = 0, []; 		Z(0, 1) = 1, 2k - 1,
     Z[1, 0] = 1, 2k - 2;	Z(1, 1) = 2k, 2k - 1,

     Z = Matrix[k x (l + k - 2) // (k - 1)], where v-max = (l + k-2) // k-1
     Z[u, v] = n[v(k-1) + u] if v is even
     Z[u, v] = n[v(k-1) + k-1 - u] if v is odd
     
     so: Z[u, v] = n[v(k-1) + (v%2) * (k-1 - 2u) + u]
     </pre>
     * <p>O(N)</p>
     * Runtime: 4 ms, faster than 79.54% of Java online submissions for ZigZag Conversion.<br>
     * Memory Usage: 37.5 MB, less than 98.94% of Java online submissions for ZigZag Conversion.
     * @param s
     * @param k
     * @return
     */
    public String convert(String s, int k) {
    	if (s == null || s.length() <= k || k < 2)
    		return s;

    	StringBuffer z = new StringBuffer();
    	int l = s.length();
		int vmax = (l + k - 2) / (k - 1);

   		for (int u = 0; u < k; u++) {
   			for (int v = 0; v <= vmax; v++) {
   				if (v % 2 == 0) {
   					int at = v * (k-1) + u;
					if (at >= l)
					   break;
					else if (u != k-1)
						z.append(s.charAt(v * (k - 1) + u));
   				}
   				else {
   					int at = v * (k-1) + k-1 - u;
					if (at >= l)
						break;
					else if (u != 0)
						z.append(s.charAt(v * (k-1) + k-1 - u));
   				}
    		}
    	}
   		
   		return z.toString();
    }
}
