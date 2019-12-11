package leetcode.string.q004_palindrome;

/**
 * 5. Longest Palindromic Substring
 * https://leetcode.com/problems/longest-palindromic-substring/
 * 
 * Runtime: 6 ms, faster than 87.86% of Java online submissions for Longest Palindromic Substring.
 * Memory Usage: 36.1 MB, less than 100.00% of Java online submissions for Longest Palindromic Substring.
 * 
 * @author odys-z@github.com
 *
 */
public class Solution {
	class PolinStr {
		private String raw;
		private int rawLen;

		PolinStr(String raw) {
			this.raw = raw;
			this.rawLen = raw == null ? 0 : raw.length();
		}
		
		int len() {
			return this.raw == null ? 0 : rawLen * 2 + 1;
		}
		
		char at(int ix) {
			if (ix < 0)
				return '$';
			else if (ix > rawLen * 2)
				return '%';
			else if ((ix & 1) == 0)
				return '#';
			else
				return raw == null ? null : raw.charAt(ix / 2);
		}

		public String sub(int l, int r) {
			return raw.substring(l < 0 ? 0 : l >> 1, r >> 1);
		}
	}

    public String longestPalindrome(String s) {
        PolinStr poln = new PolinStr(s);
        int c = 0;
        int R = 0;
        
        int slen = poln.len();
        int[] p = new int[slen];
        
        int maxl = 0; 
        int maxLen = 0;

        for (int i = 0; i < slen; i++) {
        	int mirr = 2 * c - i;
        	mirr = mirr >= 0 ? mirr : 0;
        	p[i] = Math.min(p[mirr], R > i ? R - i : 0);
        	
        	int l = i - p[i] - 1;
        	int r = i + p[i] + 1;
        	
        	while (poln.at(l) == poln.at(r)) {
        		p[i]++;
        		l--;
        		r++;
        	}
        	
        	if (i + p[i] >= R) {
        		R = i + p[i];
        		c = i;
        	}
        	
        	if (maxLen < p[i]) {
        		maxLen = p[i];
        		maxl = l + 1;
        	}
        }

        int maxr = maxl + 1 + 2 * maxLen;
        return poln.sub(maxl, maxr);
    }
}
