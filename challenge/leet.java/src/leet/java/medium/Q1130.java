package leet.java.medium;

public class Q1130 {
	public int mctFromLeafValues(int[] arr) {
	    int res = 0;
	    while (arr.length >= 2) {
	    	int min = Integer.MAX_VALUE;
	    	int replace = 0;
	    	int mnx = -1;
	    	for (int i = 1; i < arr.length; i++) {
	    		if (min > arr[i-1] * arr[i]) {
	    			min = arr[i-1] * arr[i];
	    			replace = Math.max(arr[i-1], arr[i]);
	    			mnx = i;
	    		}
	    	}
	    	res += min;
	    	int[] arr_ = new int[arr.length - 1];
	    	System.arraycopy(arr, 0, arr_, 0, mnx - 1);
	    	arr_[mnx-1] = replace;
	    	System.arraycopy(arr, mnx+1, arr_, mnx, arr.length - mnx - 1);
	    	arr = arr_;
	    }
		return res;
	}
}
