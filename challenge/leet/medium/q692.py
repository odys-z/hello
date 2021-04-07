'''
'''
from unittest import TestCase
from typing import List
import heapq

class Solution():
    '''
    Runtime: 60 ms, faster than 30.47% of Python3 online submissions for Top K Frequent Words.
    Memory Usage: 14.6 MB, less than 10.25% of Python3 online submissions for Top K Frequent Words.
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = dict.fromkeys(words)
        for w in words:
            c = counter.get(w)
            if c == None:
                c = 1
            else: c += 1
            counter.update({w: c})
        
        q = []
        heapq.heapify(q)
        for w in counter:
            heapq.heappush(q, (-counter[w], w))

        nlarge = heapq.nsmallest(k, q)
        res = []
        for large in nlarge:
            res.append(large[1])
        return res


if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(["i", "love"],
                  s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2))
    t.assertEqual(['the', 'is', 'sunny', 'day'],
                  s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
    
    print('OK!')