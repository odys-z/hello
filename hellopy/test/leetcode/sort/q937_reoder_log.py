'''
Created on 13 Nov 2019
937. Reorder Data in Log Files


@author: ody
'''
import unittest
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def withLogid(log):
            lid, l = log.split(' ', 1)
            return (0, l, lid) if len(l[0]) > 0 and l[0].isalpha() else (1, )
        
        # return sorted(logs, key = withLogid) # 48 ms
        logs.sort(key = withLogid) # 32 ms
        return logs
        
        
class Test(unittest.TestCase):


    def test937(self):
        sl = Solution()
        
        s = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        self.assertEqual(["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"],
                          sl.reorderLogFiles(s))
        
        s = ["l5sh 6 3869 08 1295", "16o 94884717383724 9", "43 490972281212 3 51",
             "9 ehyjki ngcoobi mi", "2epy 85881033085988", "7z fqkbxxqfks f y dg",
             "9h4p 5 791738 954209", "p i hz uubk id s m l", "wd lfqgmu pvklkdp u",
             "m4jl 225084707500464", "6np2 bqrrqt q vtap h", "e mpgfn bfkylg zewmg",
             "ttzoz 035658365825 9", "k5pkn 88312912782538", "ry9 8231674347096 00",
             "w 831 74626 07 353 9", "bxao armngjllmvqwn q", "0uoj 9 8896814034171",
             "0 81650258784962331", "t3df gjjn nxbrryos b"]
        self.assertEqual(['bxao armngjllmvqwn q', '6np2 bqrrqt q vtap h', '9 ehyjki ngcoobi mi',
                          '7z fqkbxxqfks f y dg', 't3df gjjn nxbrryos b', 'p i hz uubk id s m l',
                          'wd lfqgmu pvklkdp u', 'e mpgfn bfkylg zewmg', 'l5sh 6 3869 08 1295',
                          '16o 94884717383724 9', '43 490972281212 3 51', '2epy 85881033085988',
                          '9h4p 5 791738 954209', 'm4jl 225084707500464', 'ttzoz 035658365825 9',
                          'k5pkn 88312912782538', 'ry9 8231674347096 00', 'w 831 74626 07 353 9',
                          '0uoj 9 8896814034171', '0 81650258784962331'],
                          sl.reorderLogFiles(s))

        s = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
        self.assertEqual(["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"],
                         sl.reorderLogFiles(s))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()