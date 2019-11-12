'''
Created on 13 Nov 2019
937. Reorder Data in Log Files


@author: ody
'''
import unittest
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        pass
        
        
class Test(unittest.TestCase):


    def test937(self):
        sl = Solution()
        
        s = ["l5sh 6 3869 08 1295", "16o 94884717383724 9", "43 490972281212 3 51",
             "9 ehyjki ngcoobi mi", "2epy 85881033085988", "7z fqkbxxqfks f y dg",
             "9h4p 5 791738 954209", "p i hz uubk id s m l", "wd lfqgmu pvklkdp u",
             "m4jl 225084707500464", "6np2 bqrrqt q vtap h", "e mpgfn bfkylg zewmg",
             "ttzoz 035658365825 9", "k5pkn 88312912782538", "ry9 8231674347096 00",
             "w 831 74626 07 353 9", "bxao armngjllmvqwn q", "0uoj 9 8896814034171",
             "0 81650258784962331", "t3df gjjn nxbrryos b"]
        s = sl.reorderLogFiles(s)
        print(s)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()