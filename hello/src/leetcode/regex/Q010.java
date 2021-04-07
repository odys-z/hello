package leetcode.regex;

/** 
 * 10. Regular Expression Matching
 * 
 * https://leetcode.com/problems/regular-expression-matching/solution/
 * <pre>
	Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.
	The matching should cover the entire input string (not partial).

	Note:

	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like . or *.

	Example 1:
	Input: s = "aa" p = "a"
	Output: false
	Explanation: "a" does not match the entire string "aa".

	Example 2:
	Input: s = "aa" p = "a*"
	Output: true
	Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

	Example 3:
	Input: s = "ab" p = ".*"
	Output: true
	Explanation: ".*" means "zero or more (*) of any character (.)".

	Example 4:
	Input: s = "aab" p = "c*a*b"
	Output: true
	Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

	Example 5:
	Input: s = "mississippi" p = "mis*is*p*."
	Output: false
	</pre>
 * @author odys-z@github.com
 *
 */
public class Q010 {

	/**
	 * Runtime: 69 ms, faster than 10.85% of Java online submissions for Regular Expression Matching.
	 * Memory Usage: 39.7 MB, less than 37.37% of Java online submissions for Regular Expression Matching.
	 * @param s
	 * @param p
	 * @return
	 */
	public boolean isMatch1(String s, String p) {
		int slen = s == null ? 0 : s.length();
		if (p == null || p.length() == 0)
			return s == null || slen == 0;

		char p0 = p.charAt(0);
		boolean m0 = s != null && slen > 0
					&& (p0 == s.charAt(0) || p0 == '.');
		
		if (p.length() > 1 && p.charAt(1) == '*')
			return isMatch1(s, p.substring(2))
					|| (m0 && slen > 0 && isMatch1(s.substring(1), p));
		else return m0 && slen > 0 && isMatch1(s.substring(1), p.substring(1));
	}

	/**Remove substring orperations.
	 * 
	 * Runtime: 24 ms, faster than 33.31% of Java online submissions for Regular Expression Matching.
	 * Memory Usage: 38 MB, less than 47.47% of Java online submissions for Regular Expression Matching.
	 * @param s
	 * @param p
	 * @return
	 */
	public boolean isMatch2(String s, String p) {
		int slen = s == null ? 0 : s.length();
		int plen = p == null ? 0 : p.length();
		if (plen == 0)
			return slen == 0;
		
		return match(s, 0, slen, p, 0, plen);
	}
	
	private boolean match(String s, int sx, int slen, String p, int px, int plen) {
		if (px >= plen) return sx >= slen;
		if (sx >= slen)
			// now, px < plen, only ".*.*..." is ok
			return px + 2 <= plen && p.charAt(px + 1) == '*' && match(s, sx, slen, p, px + 2, plen);
		char p0 = p.charAt(px);

		boolean m0 = slen > 0 && (p0 == s.charAt(sx) || p0 == '.');
		
		if (px + 1 < plen && p.charAt(px + 1) == '*')
			return match(s, sx, slen, p, px + 2, plen)
					|| (m0 && match(s, sx+1, slen, p, px, plen));
		else return
			m0 && (sx+1 < slen ? match(s, sx+1, slen, p, px+1, plen) : 
								match("", 0, 0, p, px+1, plen));
	}
	
	private int slen = 0;
	private int plen = 0;
	private String s;
	private String p;
	private Boolean[][] ij;
	/**DP
	 * Runtime: 1 ms, faster than 100.00% of Java online submissions for Regular Expression Matching.
	 * Memory Usage: 39.3 MB, less than 43.43% of Java online submissions for Regular Expression Matching.
	 * @param s
	 * @param p
	 * @return
	 */
	public boolean isMatch(String s, String p) {
		slen = s == null ? 0 : s.length();
		plen = p == null ? 0 : p.length();
		if (plen == 0)
			return slen == 0;
		
		this.s = s;
		this.p = p;
		this.ij = new Boolean[this.slen+1][this.plen+1];
		return matchDp(0, 0);
	}

	private boolean matchDp(int i, int j) {
		if (ij[i][j] == null) {
			if (j >= plen) return i >= slen;
			else if (i >= slen)
				return j+2 <= plen && p.charAt(j+1) == '*' && matchDp(i, j+2);
			else {
				char p0 = p.charAt(j);
				// m0
				boolean m0 = slen > 0 && (p0 == s.charAt(i) || p0 == '.');
				
				if (j+1 < plen && p.charAt(j+1) == '*')
					ij[i][j] = matchDp(i, j+2)
								|| m0 && matchDp(i+1, j);
				else ij[i][j] = m0 && matchDp(i+1, j+1);
			}
		}
		return ij[i][j];
	}
}
