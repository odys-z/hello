package leet.java.medium;

import java.util.ArrayList;
import java.util.List;

/**<a href='https://leetcode.com/problems/letter-case-permutation/'>
 * 784. Letter Case Permutation</a>
 * 
 * @author Odys Zhou
 */
public class Q784 {
    public List<String> letterCasePermutation(String S) {
    	return btrack(S);
    }

	/** 49.34% 
	 * @param s
	 * @return
	 */
	private List<String> btrack(String s) {
    	List<String> res = new ArrayList<String>();
    	int l = s.length();
    	if (l == 0) {
    		res.add("");
    		return res;
    	}
    	String last = s.substring(l - 1, l);
    	List<String> tracks = btrack(s.substring(0, s.length() - 1));
		boolean isdigit = false;
		try {
			Integer.valueOf(last);
			isdigit = true;
		} catch(Exception e) {}
    	for (String t : tracks) {
    		if (isdigit)
    			res.add(t + last);
    		else {
    			res.add(t + last.toLowerCase());
    			res.add(t + last.toUpperCase());
    		}
    	}
		return res;
	}


}
