from unittest import TestCase
from typing import List
import sys

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        
        while len(arr) >= 2:
            minV, idx = sys.maxsize, -1
            for i in range(1,len(arr)):
                if arr[i] * arr[i-1] < minV:
                    minV = arr[i] * arr[i-1]
                    idx = i
            res += minV
            arr = arr[:idx-1] + [max(arr[idx-1], arr[idx])] + arr[idx+1:]
                 
        return res

if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(32, s.mctFromLeafValues([6,2,4]))
    t.assertEqual(315, s.mctFromLeafValues([6,1,5,5,5,5,5,15,6]))
    
    print('OK!')

'''
    c#
public static class hlp {
    public static T[] cut<T>(this T[] array, int cuti, T replace) {
        T[] result = new T[array.Length - 1];
        Array.Copy(array, 0, result, 0, cuti - 1);
        result[cuti-1] = replace;
        Array.Copy(array, cuti + 1, result, cuti, array.Length - cuti - 1);
        return result;
    }
}

public class Solution {
    public int MctFromLeafValues(int[] arr) {
        int res = 0;
        while (arr.Length >= 2) {
            int min = int.MaxValue;
            int mnx = -1;
            int replace = 0;
            for (int i = 1; i < arr.Length; i++) {
                if (min > arr[i-1] * arr[i]) {                    
                    min = arr[i-1] * arr[i];
                    mnx = i;
                    replace = Math.Max(arr[i-1], arr[i]);
                }                
            }
            res += min;
            arr = hlp.cut<int>(arr, mnx, replace);
        }
        return res;
    }
}
'''
