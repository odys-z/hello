'''
1710. Maximum Units on a Truck
https://leetcode.com/problems/maximum-units-on-a-truck/


Created on 27 Nov 2021
@author: Odys Zhou
'''

from typing import List
from unittest.case import TestCase

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key = lambda boxtype: boxtype[1], reverse = True)
        load, loadbox, x, checkLast = 0, 0, 0, False

        for x in range(len(boxes)):
            box = boxes[x]
            if loadbox + box[0] > truckSize:
                checkLast = True
                break

            load += box[0] * box[1]
            loadbox += box[0]
        
        if checkLast:
            box = boxes[x]
            c = min(truckSize - loadbox, box[0])
            load += c * box[1]
            
        return load


        
if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    t.assertEqual(1 , s.maximumUnits([[1, 1]], 1))
    t.assertEqual(2 , s.maximumUnits([[1, 1], [2, 2]], 1))
    t.assertEqual(8 , s.maximumUnits([[1, 3], [2, 2], [3, 1]], 4))
    t.assertEqual(10, s.maximumUnits([[1, 10]], 10))
    
    print('OK')