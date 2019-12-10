package leetcode.string.q004_palindrome;

/**
 * 5. Longest Palindromic Substring
 * https://leetcode.com/problems/longest-palindromic-substring/
 * 
 * @author odys-z@github.com
 *
 */
public class Solution {
	class Polindrome {
		private String raw;

		Polindrome(String raw) {
			this.raw = raw;
		}
		
		int len() {
			return this.raw == null ? 0 : raw.length() * 2 + 1;
		}
		
		char at(int ix) {
			if ((ix & 1) == 0)
				return '#';
			else
				return raw == null ? null : raw.charAt(ix / 2);
		}

		public String sub(int l, int r) {
			return raw.substring(l >> 1, r >> 1);
		}
	}

    public String longestPalindrome(String s) {
        Polindrome poln = new Polindrome(s);
        int c = 0;
        int r = 0;
        
        int slen = poln.len();
        int[] p = new int[slen];
        
        int maxl = 0; 
        int maxr = 0;

        while (c < slen) {
        	poln.at(c);
        }

        return poln.sub(maxl, maxr);
    }
}
