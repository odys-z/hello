'''
401. Binary Watch
https://leetcode.com/problems/binary-watch/

A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on
the right.

hour    8   4   2   1
        -------------
        0   0   x   x
    
minute  32 16 8  4  2  1
        ----------------
        0  x  x  0  0  x
    
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that
are currently on, return all possible times the watch could represent.

Example:
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:
The order of output does not matter.

The hour must not contain a leading zero, for example "01:00" is not
valid, it should be "1:00".

The minute must be consist of two digits and may contain a leading zero,
for example "10:2" is not valid, it should be "10:02".
'''
from unittest import TestCase
from typing import List

class Solution:
    '''
    74.93%
    '''
    def readBinaryWatch(self, num: int) -> List[str]:
        # times: xxxx xxxxxx
        def times(n, digits):
            if digits < n:
                return []
            elif n == 0 or digits == 0:
                return [0]

            # 0 xxxxx...
            res0 = times(n, digits-1)

            # 1 xxx...
            t0 = 2**(digits-1)
            res1 = times(n-1, digits-1)
            for t1 in res1:
                res0.append(t1 + t0)

            return res0
        
        def convert(ts: List[int]) -> List[str]:
            res = []
            for t in ts:
                h = t // 0x40
                m = t & 0x3f
                if m < 60 and h < 12:
                    res.append(f"{h:d}:{m:02d}")
            return res

        return convert(times(num, 10))

        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertCountEqual(["0:00"], s.readBinaryWatch(0))
    t.assertCountEqual(["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"],
                       s.readBinaryWatch(1))
    t.assertCountEqual(["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"],
                       s.readBinaryWatch(2))

    t.assertCountEqual(["7:31","7:47","7:55","7:59","11:31","11:47","11:55","11:59"],
                       s.readBinaryWatch(8))

    t.assertCountEqual([], s.readBinaryWatch(9))
    print('OK!')
