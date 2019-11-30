'''
Created on 10 Nov 2019

@author: ody
'''

import itertools as it
import collections
import heapq

class ITool(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def simple_acc(self, initv):
        rep = it.repeat(initv)
        i = it.accumulate(rep, lambda e, _ = 0 : e + _)
        for _ in range(10):
            print(next(i))
    
    def topKFreq(self, nums, k):
        count = collections.Counter(nums)   
        print(count)
        return heapq.nlargest(k, count.keys(), key=count.get) 

    def second_order(self, p, q, r, initial_values):
        ''' Return sequence defined by
            s(n) = p * s(n-1) + q * s(n-2) + r.
        '''
        intermediate = it.accumulate(
            it.repeat(initial_values),
            lambda s, _: (s[1], p*s[1] + q*s[0] + r)
        )
        return map(lambda x: x[0], intermediate)
        
