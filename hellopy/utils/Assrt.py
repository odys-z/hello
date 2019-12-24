'''
Created on 22 Dec 2019

@author: ody
'''

from typing import List
from collections import defaultdict
import re

class AssertErr(AssertionError):
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
            raise AssertErr("len(a) != len(b):\n{}\n{}".format(a, b))

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
                    deletings.append(arr2)
            else:
                raise AssertErr('Sencond array has element not found in first\n%s\n^\n%s'
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
            raise AssertErr('Some element not matched:\n%s\n %s'
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

    def int2dArrFile(self, fpath, dim = 2, ignoreElementOrder = True):
        with open(fpath, 'r') as f:
            xpect = None;
            ln = '#'
            while ln:
                if ln[0] in '#\n':
                    ln = f.readline()
                    continue

                if not xpect:
                    xpect = ln
                else:
                    xd = XdArrParser(dim)
                    a = xd.parseInt(xpect)
                    b = xd.parseInt(ln)
                    self.int2dArr(a, b, ignoreElementOrder)
                    xpect = None

                ln = f.readline()


class XdArrParser(object):
    def __init__(self, dimension):
        self.dim = dimension
        
    def parseInt(self, istr: str) -> List[List[int]]:
        arr, __ = self.xdInt(istr, 0, 0)
        return arr[0]

    def xdInt(self, istr: str, dim: int, start: int) -> (List[List[int]], int):
        ix = start
        l = len(istr)
        lst = None
        while ix < l:
            if dim < self.dim and istr[ix] == '[':
                # parse first child
                lst = list()
                inums, ix = self.xdInt(istr, dim + 1, ix + 1)
                lst.append(inums)
                start = ix + 1

            elif dim < self.dim and istr[ix] == ',':
                # parse siblings
                if not lst:
                    raise AssertErr("parse error at {}".format(ix))
                while istr[ix] != '[':
                    ix += 1
                inums, ix = self.xdInt(istr, dim + 1, ix + 1)
                lst.append(inums)
                start = ix + 1

            elif dim == self.dim:
                # parse a 1-d array
                while istr[ix] != ']':
                    ix += 1
                if start < ix:
                    inums = list(map(int, re.split(r'[\"\']? *, *[\"\']?', istr[start : ix])))
                    return inums, ix
                elif start == ix:
                    return [], ix

            ix += 1

        return lst, ix

        
        
    