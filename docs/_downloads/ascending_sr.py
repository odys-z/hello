'''
2016 - 2017 ACSL American Computer Science League
SENIOR DIVISION

Contest #2 ASCENDING STRINGS
'''
from unittest import TestCase

def atFirst(snum):
    '''
        First thoughts
    '''
    h, r = 0, len(snum)
    res = []
    while r > h: 
        # forward 
        res.append(int(snum[s:e]))
        # backward
        res.append(int(snum[s:e:-1]))
    return res

def parsNums(snum):
    def cutforth(snum, h, r, maxn):
        if h >= r: return None, h
        l = 1
        n = int(snum[h : h + l])
        if not maxn: return n, h + 1
        while n <= maxn and h + l < r:
            l += 1
            n = int(snum[h : h + l])
        return n if h + l <= r and n > maxn else None, h + l
    
    def cutback(snum, h, r, maxn):
        if h >= r: return None, r
        l = 1
        n = int(snum[r - 1 : r - l - 1 : -1])
        if not maxn: return n, r - 1
        while n <= maxn and h + l < r:
            l += 1
            n = int(snum[r - 1 : r - l - 1 : -1])
        return n if h + l <= r and n > maxn else None, r - l

    h, r = 0, len(snum)
    res = []
    n = None

    while r > h: 
        # forward, backward
        n, h = cutforth(snum, h, r, n)
        
        if n == None: break
        res.append(n)

        n, r = cutback(snum, h, r, n)

        if n == None: break
        res.append(n)

    return res

if __name__ == "__main__":
    t = TestCase()
    t.assertCountEqual([3, 8, 14, 35, 159], parsNums('31415926538'))
    t.assertCountEqual([3, 5, 14, 62, 159], parsNums('314159265'))
    t.assertCountEqual([2, 7, 16], parsNums('201617'))
    t.assertCountEqual([1, 9, 23, 87, 456], parsNums('123456789'))
    t.assertCountEqual([1, 4, 22, 44, 333], parsNums('1223334444'))
    
    t.assertCountEqual([2, 8, 71, 281, 828], parsNums('2718281828'))
    t.assertCountEqual([1, 12, 22, 23], parsNums('12233221'))
    t.assertCountEqual([5, 50], parsNums('5005'))
    t.assertCountEqual([2, 5], parsNums('250'))
    t.assertCountEqual([9], parsNums('9'))

    print('OK!')
