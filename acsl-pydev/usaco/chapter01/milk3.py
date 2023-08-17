'''
ID: odys.zh1
LANG: PYTHON3
TASK: milk3
'''

from typing import List

class Milk3:
    def prog(self, buckets: (int, int, int)):
        walked = set()
        
        def ifPossible(sm, distbuk, dm):
            return min(distbuk - dm, sm)
        
        def possiblePours(buckets, state):
            pos = set()
            a, b, c = buckets
            ma, mb, mc = state
            '''
            a -> b, a -> c
            b -> a, b -> c
            c -> a, c -> b
            '''
            amount = ifPossible(ma, b, mb)
            if amount > 0:
                pos.add((ma - amount, mb + amount, mc))

            amount = ifPossible(ma, c, mc)
            if amount > 0:
                pos.add((ma - amount, mb, mc + amount))

            amount = ifPossible(mb, a, ma)
            if amount > 0:
                pos.add((ma + amount, mb - amount, mc))

            amount = ifPossible(mb, c, mc)
            if amount > 0:
                pos.add((ma, mb - amount, mc + amount))

            amount = ifPossible(mc, a, ma)
            if amount > 0:
                pos.add((ma + amount, mb, mc - amount))

            amount = ifPossible(mc, mb, mb)
            if amount > 0:
                pos.add((ma, mb + amount, mc - amount))
            return pos

        def pour(buckets, state):
            walked.add(state)

            possibles = possiblePours(buckets, state)
            for possib in possibles:
                if possib not in walked:
                    pour(buckets, possib) 
        
        milks = (0, 0, buckets[2])
        pour(buckets, milks)
        ans = set()
        for s in walked:
            if s[0] == 0:
                ans.add(s[2])
        return sorted(list(ans))

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    m = Milk3() 

    t.assertCountEqual([1, 2, 8, 9, 10],
                       m.prog([8, 9, 10]))

    t.assertCountEqual([5, 6, 7, 8, 9, 10],
                       m.prog([2, 5, 10]))
    print('OK!')

else:
    def outputLines(intArr2: List[int]) -> int:
        f = open('milk3.out', 'w')
        f.write(' '.join(map(lambda x: str(x), intArr2)))
        f.write('\n')
        f.close()
        return len(intArr2)
 
    g = Milk3()
    fin = open('milk3.in', 'r')
    l = fin.readline().split()
    fin.close()
    A, B, C = int(l[0]), int(l[1]), int(l[2])

    ans = g.prog((A, B, C))
    outputLines(ans)
