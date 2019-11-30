'''
A heap with key lambda.
See https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate

Created on 27 Nov 2019

@author: odys-z@github.com
'''
from heapq import heapify, heappush, heappop

class Heapk(object):
    '''
        A python heapq wrapper that can accept key lambda.
        For necessity, See https://stackoverflow.com/questions/8875706/heapq-with-custom-compare-predicate
    '''
    def Inc():  # @NoSelf
        i = 0
        while True:
            yield i
            i += 1
    
    inc = Inc();

    def __init__(self, dat = [], key = lambda x : x):
        '''
        Constructor
        '''
        if len(dat) > 0:
            pass
        else: self.hp = []
        self.hp = [(key(e), next(Heapk.inc), e) for e in dat]
        heapify(self.hp)
        self.key = key
    
    def push(self, e):
        heappush(self.hp, (self.key(e), next(Heapk.inc), e))
    
    def pop(self):
        head = heappop(self.hp)
        if head: return head[2]
        else: return None
        
    def len(self):
        return len(self.hp)
    