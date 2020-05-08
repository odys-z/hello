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
	public boolean isMatch(String s, String p) {
		int slen = s == null ? 0 : s.length();
		if (p == null || p.length() == 0)
			return s == null || slen == 0;

		char p0 = p.charAt(0);
		boolean m0 = s != null && slen > 0
					&& (p0 == s.charAt(0) || p0 == '.');
		
		if (p.length() > 1 && p.charAt(1) == '*')
			return isMatch(s, p.substring(2))
					|| (m0 && slen > 0 && isMatch(s.substring(1), p));
		else return m0 && slen > 0 && isMatch(s.substring(1), p.substring(1));
	}
}
