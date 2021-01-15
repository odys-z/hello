from unittest import TestCase
from typing import List
from utils.assertHelper import assertStrsEqual

class Solution:
    '''
    Runtime: 84 ms, faster than 99.00% of Python3 online submissions for Group Anagrams.
    Memory Usage: 17.1 MB, less than 81.30% of Python3 online submissions for Group Anagrams.
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        
        for s in strs:
            k = ''.join(sorted(s))
            ana = res.get(k, [])
            ana.append(s)
            res.update({k: ana})
        
        return list(res.values())

if __name__ == '__main__':
    t = TestCase()
    s = Solution()
    
    # t.assertCountEqual([["bat"],["nat","tan"],["ate","eat","tea"]],
    #                    s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    
    expct = [["bat"],["nat","tan"],["ate","eat","tea"]]
    assertStrsEqual(expct,
                    s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    
    print("OK!")