package leetcode.array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * https://leetcode.com/problems/3sum/submissions/
 * 
 * @author odys-z@github.com
 *
 */
public class Q015_3sum {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        int n = nums.length;
        Arrays.sort(nums);   // O(nlogn)
        if(n < 3)return list;
        
        for(int i = 0; i < n - 2; i++) {
            if(i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                int low = i + 1;
                int high = n - 1;
                int sum = 0 - nums[i];
                
                while(low < high){
                    if(nums[low] + nums[high] == sum){
                        list.add(Arrays.asList(nums[i], nums[low], nums[high]));
                        while(low < high && nums[low] == nums[low+1]) low++;             //skip duplicates
                        while(low < high && nums[high] == nums[high-1]) high--;           //skip duplicates
                        low++;
                        high--;
                    }
                    else if(nums[low] + nums[high] > sum){
                        high--;
                    }
                    else{
                        low++;
                    }
                }
            }
            
        }
        return list;
    }
    
    /**Failed
     * @param nums
     * @return
     */
    public List<List<Integer>> threeSum2(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        int n = nums.length;
        Arrays.sort(nums);   // O(nlogn)
        if(n < 3) return list;
        
		int lo = 1;
		int hi = n - 1;

        	// first round, get the low, high initiated   
            int sum = - nums[0];
            {
                while(lo < hi){
                    if(nums[lo] + nums[hi] == sum){
                        list.add(Arrays.asList(-sum, nums[lo], nums[hi]));	// n3 <= nlow <= nheigh
                        while(lo < hi && nums[lo] == nums[lo+1]) lo++;  	// skip duplicates
                        while(lo < hi && nums[hi] == nums[hi-1]) hi--;		// skip duplicates
                        lo++;
                        hi--;
                    }
                    else if(nums[lo] + nums[hi] > sum){
                    	hi--;
                    }
                    else{
                    	lo++;
                    }
                }
            }
            if (n < 4) return list;

            if (lo == 1) lo++;
            while (lo >= hi) hi++;
            if (hi >= n) {
            	hi = n - 1;
            	lo = hi - 1;
            };
            
            // now move lo, hi without unnecessary moving
            for (int i3 = 1; i3 < n - 2; i3++) {
            	if (hi >= n)
            		break;
            	if (i3 + 1 >= lo)
            		lo = i3 + 1;
            	sum = - nums[i3];
            	int s2_3 = nums[lo] + nums[hi]; // s2_3 > sum (initial)
				if(s2_3 == sum) {
					list.add(Arrays.asList(-sum, nums[lo], nums[hi]));	// n3 <= nlow <= nheigh
					while(i3 < lo && nums[lo] == nums[lo+1]) lo--;  	// skip duplicates
					while(hi < n  && nums[hi] == nums[hi-1]) hi++;		// skip duplicates
					lo--;
					hi++;
				}
				else {
					if(s2_3 > sum){
						while (i3 < lo && s2_3 > sum && lo < hi) {
							int dlo = nums[lo] - nums[lo - 1];
							int dhi = nums[hi] - nums[hi - 1];
							if (i3 + 1 < lo && (dlo <= dhi || lo + 1 == hi))
								lo--;
							else if (i3 < lo && lo + 1 < hi )
								hi--;
							else break;
							s2_3 = nums[lo] + nums[hi];
						}

						if(i3 < lo && lo < hi && nums[lo] + nums[hi] == sum) {
							list.add(Arrays.asList(-sum, nums[lo], nums[hi]));	// n3 <= nlow <= nheigh
							while(i3 < lo && nums[lo] == nums[lo+1]) lo--;  	// skip duplicates
							while(hi < n  && nums[hi] == nums[hi-1]) hi++;		// skip duplicates
							if (i3 + 1 < lo)
								lo--;
							if (hi < n - 1)
								hi++;
						}
					}
				}
            }
            
        return list;
    }
    
	public List<List<Integer>> threeSum3(int[] nums) {
		if (nums.length < 3)
			return Collections.emptyList();
		List<List<Integer>> res = new ArrayList<>();
		int minValue = Integer.MAX_VALUE;
		int maxValue = Integer.MIN_VALUE;
		int negSize = 0;
		int posSize = 0;
		int zeroSize = 0;
		for (int v : nums) {
			if (v < minValue)
				minValue = v;
			if (v > maxValue)
				maxValue = v;
			if (v > 0)
				posSize++;
			else if (v < 0)
				negSize++;
			else
				zeroSize++;
		}
		if (zeroSize >= 3)
			res.add(Arrays.asList(0, 0, 0));
		if (negSize == 0 || posSize == 0)
			return res;
		if (minValue * 2 + maxValue > 0)
			maxValue = -minValue * 2;
		else if (maxValue * 2 + minValue < 0)
			minValue = -maxValue * 2;

		int[] map = new int[maxValue - minValue + 1];
		int[] negs = new int[negSize];
		int[] poses = new int[posSize];
		negSize = 0;
		posSize = 0;
		for (int v : nums) {
			if (v >= minValue && v <= maxValue) {
				if (map[v - minValue]++ == 0) {
					if (v > 0)
						poses[posSize++] = v;
					else if (v < 0)
						negs[negSize++] = v;
				}
			}
		}
		Arrays.sort(poses, 0, posSize);
		Arrays.sort(negs, 0, negSize);
		int basej = 0;
		for (int i = negSize - 1; i >= 0; i--) {
			int nv = negs[i];
			int minp = (-nv) >>> 1;
			while (basej < posSize && poses[basej] < minp)
				basej++;
			/* basej is not searched every time
			if (minp != 0 && map[minp - minValue] > 0)
				basej = Arrays.binarySearch(poses, 0, posSize, minp);
			else
				while (basej < posSize && poses[basej] < minp)
					basej++;
			*/
			
			for (int j = basej; j < posSize; j++) {
				int pv = poses[j];
				int cv = 0 - nv - pv;
				if (cv >= nv && cv <= pv) {
					if (cv == nv) {
						if (map[nv - minValue] > 1)
							res.add(Arrays.asList(nv, nv, pv));
					} else if (cv == pv) {
						if (map[pv - minValue] > 1)
							res.add(Arrays.asList(nv, pv, pv));
					} else {
						if (map[cv - minValue] > 0)
							res.add(Arrays.asList(nv, cv, pv));
					}
				} else if (cv < nv)
					break;
			}
		}
		return res;

	}

	@SuppressWarnings("unused")
	private void twoSum(int start, int[] nums,int target,List<List<Integer>> res,Map<Integer,Integer> used){
		Map<Integer,Integer> map = new HashMap<>();
		Map<Integer,Integer> used2 = new HashMap<>();
		for (int i = start; i < nums.length; i++){
			int t = target - nums[i];
			if (map.get(t) != null && used.get(t) == null &&  used.get(nums[i]) == null){
				if (used2.get(nums[i]) == null && used2.get(t) == null){
					res.add(new ArrayList<>(Arrays.asList(nums[start-1],t,nums[i])));
					used2.put(t,1);
					used2.put(nums[i],1);
				}
			}else {
				map.put(nums[i],i);
			}
		}
	}
}
