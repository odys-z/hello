package leetcode.array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

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
        Arrays.sort(nums);   // O(nlogn)   Sort toget help in 2 sum
        if(nums.length<3)return list;
        
        //the idea is to loop through all elemnts and for every element i , perform the 2sum for (i+1)th to (n-1)th element
        for(int i=0; i<n-2 ;i++){
            
            if(i==0 || (i>0 && nums[i]!=nums[i-1])){          // for every i , do a 2sum for the rest 2 elements
                int low = i+1;
                int high = n-1;
                int sum = 0-nums[i];
                
                while(low<high){
                    if(nums[low]+nums[high]==sum){
                        list.add(Arrays.asList(nums[i], nums[low], nums[high]));
                        while(low<high && nums[low]==nums[low+1])low++;             //skip duplicates
                        while(low<high && nums[high]==nums[high-1])high--;           //skip duplicates
                        low++;
                        high--;
                    }
                    else if(nums[low]+nums[high]>sum){
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
            if (hi >= n) return list;
            
            // now move lo, hi without unnecessary moving
            for (int i3 = 1; i3 < n - 2; i3++) {
            	sum = - nums[i3];
            	int s2_3 = nums[lo] + nums[hi]; // s2_3 > sum (initial)
				if(s2_3 == sum){
					list.add(Arrays.asList(-sum, nums[lo], nums[hi]));	// n3 <= nlow <= nheigh
					while(i3 < lo && nums[lo] == nums[lo+1]) lo--;  	// skip duplicates
					while(hi < n  && nums[hi] == nums[hi-1]) hi++;		// skip duplicates
					lo--;
					hi++;
				}
				else {
					if(s2_3 > sum){
//						if (lo-1 <= i3 && hi - 1 <= lo) {
//							continue;
//						}
						hi--;
						while (i3 < lo && nums[lo] + nums[hi] > sum) {
							lo--; 
							// while(lo < hi && nums[lo] == nums[lo + 1]) lo--;// skip duplicates
						}
						if (lo == i3) {
							lo++;
							if (lo == hi)
								return list;
						}
						if (hi < n && nums[lo] + nums[hi] < sum) {
							hi++;
							while(hi < n && nums[hi] == nums[hi - 1]) hi++;		// skip duplicates
						}
					}
				}
            }
            
        return list;
    }
}
