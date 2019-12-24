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
        Arrays.sort(nums);   // O(nlogn)   Sort toget help in 2 sum
        if(n < 3)return list;
        
		int low = n / 2;
		int high = low + 1;
        //the idea is to loop through all elemnts and for every element i , perform the 2sum for (i+1)th to (n-1)th element
        for(int i = 0; i < n-2; i++){
            
            if(i == 0 || (i > 0 && nums[i] != nums[i - 1])){          // for every i , do a 2sum for the rest 2 elements
//                int low = i+1;
//                int high = n-1;
                int sum = 0 - nums[i];
                
                while(0 <= low && high < n){
                    if(nums[low] + nums[high] == sum){
                        list.add(Arrays.asList(nums[i], nums[low], nums[high]));
                        while(low < high && nums[low] == nums[low+1]) low--;             //skip duplicates
                        while(low < high && nums[high] == nums[high-1]) high++;           //skip duplicates
                        low--;
                        high++;
                    }
                    else if(nums[low] + nums[high] > sum){
                        // high--;
                    	low--;
                    }
                    else{
                        // low++;
                    	high++;
                    }
                }
            }
            
        }
        return list;
    }
}
