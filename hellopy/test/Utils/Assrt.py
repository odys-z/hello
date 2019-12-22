'''
Created on 22 Dec 2019

@author: ody
'''

from typing import List
from collections import defaultdict
import re

class AssrtError(AssertionError):
    def __init__(self, p):
        super().__init__(p)

class Eq(object):
    '''
    '''


    def __init__(self, params = {}):  # @UnusedVariable
        ''' '''
        pass

        
    def int2dArr(self, a : List[List[int]], b : List[List[int]], ignoreElementOrder = True):
        ''' Assert 2 arrays are equal, in any order '''
        if len(a) != len(b):
            raise AssrtError("len(a) != len(b)")

        pool1 = defaultdict(list)
        for arr1 in a:
            s1 = sum(arr1)
            if arr1: arr1.sort()
            if s1 in pool1:
                pool1[s1].append(arr1)
            else: pool1.update({s1: [arr1]})
        
        deletings = []
        for arr2 in b:
            s2 = sum(arr2)
            if s2 in pool1:
                arr1s = pool1[s2]
                if self.findRemove(arr1s, arr2, ignoreElementOrder):
                    # arr1s.remove(arr2)
                    # b.remove(arr2)
                    deletings.append(arr2)
            else:
#                 raise self.a.failureException('Sencond array has element not found in first\n%s\n^\n%s'
#                                         % (arr2, a))
                raise AssrtError('Sencond array has element not found in first\n%s\n^\n%s'
                                        % (arr2, a))
        for d in deletings:
            b.remove(d);

        l1 = 0
        for v1 in pool1.values():
            l1 = l1 + len(v1)
        
        l2 = 0
        for v2 in b:
            l2 = l2 + len(v2)
        
        if l1 != 0 or l2 != 0:
#             raise self.a.failureException('Some element not matched; %s\n %s'
#                                         % (pool1.values, b))
            raise AssrtError('Some element not matched:\n%s\n %s'
                                        % (list(pool1.values()), b))
        
        
    def findRemove(self, sortedArrs, a, ignoreOrder = True) -> bool:
        a_ = a
        if ignoreOrder and a != None:
            a_ = sorted(a)
        
        for arr in sortedArrs:
            if arr == a_:
                sortedArrs.remove(arr)
                return True
        
        return False

    def int2dArrFile(self, fpath, ignoreElementOrder):
        with open(fpath, 'r') as f:
            xpect = None;
            for ln in f.readline():
                if ln[0] in '#\n':
                    continue
                if not xpect:
                    xpect = ln
                else:
                    xd = IntxdArr()
                    a = xd.parseInt(xpect)
                    b = xd.parseInt(ln)
                    self.int2dArr(a, b, ignoreElementOrder)
                    xpect = None

class IntxdArr(object):               
    def __init__(self, dimension):
        self.dim = dimension
        self.dstack = []
                    
    def parseInt(self, intStr: str) -> List[List[int]]:
        dim = 0
        l = len(intStr)
        ix = 0
        while ix < l:
            if intStr[ix] == '[':
                dim += 1
                start = ix + 1 
                self.dstack.append(list())
                if dim == self.dim:
                    while ix < l and intStr[ix] != ']':
                        ix += 1
                    inums = list(map(int, re.split(r'[\"\']? *, *[\"\']?', intStr[start : ix])))
            elif intStr[ix] == ']':
                dim -= 0
                if dim < 0:
                    raise AssrtError("Parse error: unmatched ']' arroud {}".format(ix))
                self.dstack.pop()
                self.dstack[-1].append(inums)
            elif intStr[ix] == ' ' or intStr[ix] == ',':
                pass

            ix += 1

        return self.dstack[0]
