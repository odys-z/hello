package leet.java.medium;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 78. <a href='https://leetcode.com/problems/subsets/'>Subsets</a>
 * 
 * 1ms 64.24%
 * 
 * @author Odys Zhou
 */
public class Q078 {
    @SuppressWarnings({ "unchecked", "rawtypes" })
	public List<List<Integer>> subsets(int[] nums) {
    	List<List<Integer>> res = new ArrayList<List<Integer>>();
    	if (nums.length == 0) {
    		List<Integer> zero = new ArrayList();
    		res.add(zero);
    		return res;
    	}
    	else if (nums.length == 1) {
    		List<Integer> zero = new ArrayList();
    		res.add(zero);
    		List<Integer> one = new ArrayList();
    		one.add(nums[0]);
    		res.add(one);
    		return res;
    	}
    	
    	List<List<Integer>> backtrackings = subsets(Arrays.copyOfRange(nums, 0, nums.length - 1));
    	
    	for (List<Integer> trck : backtrackings) {
    		ArrayList trk = (ArrayList) ((ArrayList) trck).clone();
    		trk.add(nums[nums.length - 1]);
    		res.add(trk);
    	}
    	res.addAll(backtrackings);

        return res;
    }
}
