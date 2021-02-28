'''
SAMPLE INPUT:
    MBAMMDXXMMMGGMMZ 3
    MHHHHJLDDHHDDD 3
    THETENNESSEEVOLUNTEERS 2
    MISSISSIPPI 3
    BOOOKEEEPEEERR 4

EXPECTED OUTPUT:
    MMMGGMMMXXABDMZ
    HHHDDDHHJLM
    EENNSSEEHLNORSTTUV
    PPSSSIIIM
    EEEEOOORRBKP
'''
from unittest import TestCase
import heapq

class SolutionList:
    def trans(self, s, maxchar):
        lst = []
        c, span = s[0], 1
        for nxt in s[1:]:
            if nxt == c:
                span += 1
            else:
                lst.append((-span, c))
                c = nxt
                span = 1
        else:
            lst.append((-span, c))
        
        res = [] 
        lst.sort()
        for c, chs in lst[::]:
            if -c > maxchar:
                res.append(chs * maxchar)
            else:
                res.append(chs * (-c))
        return ''.join(res)
    
    def exced(self, s, maxchar):
        res = []
        c0, chs = '', 0
        for c in s:
            if c == c0:
                chs += 1
                if chs > maxchar:
                    continue
            else:
                c0 = c
                chs = 1
            res.append(c)
        return ''.join(res)

    def transf(self, s):
        s = s.split()
        s, maxchar = s[0], int(s[1])
        s = self.trans(s, maxchar)
        return self.exced(s, maxchar)

class SolutionHeap:
    def transf(self, s):
        s = s.split()
        s, maxchar = s[0], int(s[1])

        q = []
        start, ch = 0, s[0]
        for end in range(1, len(s)):
            c = s[end]
            if c == ch:
                continue
            else:
                l = min(end - start, maxchar)
                q.append((start - end, ch * l))
                start = end
                ch = c
        else:
            l = min(end - start + 1, maxchar)
            q.append((start - 1 - end, ch * l))
            
        
        heapq.heapify(q)
        res = []
        while len(q) > 0:
            a = heapq.heappop(q)[1]
            if len(res) > 0 and res[-1][-1] == a[0]:
                a = res.pop() + a
                res.append(a[0: min(len(a), maxchar)])
            else:
                res.append(a)
        # return ''.join(map(lambda st: st[1], q))
        return ''.join(res)


def assertEq(s):
    t = TestCase()
    t.assertEqual("MMMGGMMMXXABDMZ", s.transf('MBAMMDXXMMMGGMMZ 3'))
    t.assertEqual("HHHDDDHHJLM", s.transf('MHHHHJLDDHHDDD 3'))
    t.assertEqual("EENNSSEEHLNORSTTUV", s.transf('THETENNESSEEVOLUNTEERS 2'))
    t.assertEqual("PPSSSIIIM", s.transf('MISSISSIPPI 3'))
    t.assertEqual("EEEEOOORRBKP", s.transf('BOOOKEEEPEEERR 4'))

if __name__ == "__main__":
    s = SolutionList()
    assertEq(s)
    s = SolutionHeap()
    assertEq(s)
    
    print('OK!')
