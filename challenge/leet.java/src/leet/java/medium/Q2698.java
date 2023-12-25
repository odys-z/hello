/**
 * 2698. Find the Punishment Number of an Integer
 * https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
 */
package leet.java.medium;

import java.util.Arrays;

/**
 * https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
 */
public class Q2698 {

	static int dp[][];
	static int ans[];

	static boolean helper(String num, int target, int idx){
		if(idx >= num.length()) return target == 0;

		if(target < 0) return false;

		if(dp[idx][target] != -1) {
			System.out.println(String.format("%s %s %s", num, idx, target));
			return dp[idx][target] == 1 ? true : false; 
		}

		int sum = 0;
		for (int i = idx; i < num.length(); i++) {
			sum = sum * 10 + (num.charAt(i) - '0');

			if(helper(num, target - sum, i + 1)){
				dp[idx][target] = 1;
				return true;
			}
		}

		dp[idx][target] = 0;
		return false;
	}

	static{
		int N = (int)1e3;
		dp = new int[7][N + 1];
		ans = new int[N + 1];
		for(int i = 1; i <= N; i++){
			for(var a : dp) Arrays.fill(a, -1);
			boolean flag = helper(String.valueOf(i * i), i, 0);
			ans[i] = ans[i - 1] + (flag ? i * i : 0);
		}
	}

	public int punishmentNumber(int n) {
		return ans[n];
	}
}
