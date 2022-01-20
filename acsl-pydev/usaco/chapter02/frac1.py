'''
ID: odys.zh1
LANG: PYTHON3
TASK: frac1
'''

from typing import List

'''
       Test 1: TEST OK [0.035 secs, 9524 KB]
       Test 2: TEST OK [0.036 secs, 9448 KB]
       Test 3: TEST OK [0.035 secs, 9628 KB]
       Test 4: TEST OK [0.034 secs, 9532 KB]
       Test 5: TEST OK [0.035 secs, 9544 KB]
       Test 6: TEST OK [0.036 secs, 9532 KB]
       Test 7: TEST OK [0.036 secs, 9560 KB]
       Test 8: TEST OK [0.038 secs, 10056 KB]
       Test 9: TEST OK [0.039 secs, 10048 KB]
       Test 10: TEST OK [0.041 secs, 9980 KB]
       Test 11: TEST OK [0.059 secs, 10224 KB]

    N = 1 2 4 7 10 15 24 50 75 100 160

Python3 Russ
   Test 1: TEST OK [0.035 secs, 9628 KB]
   Test 2: TEST OK [0.035 secs, 9596 KB]
   Test 3: TEST OK [0.036 secs, 9564 KB]
   Test 4: TEST OK [0.035 secs, 9556 KB]
   Test 5: TEST OK [0.034 secs, 9540 KB]
   Test 6: TEST OK [0.035 secs, 9588 KB]
   Test 7: TEST OK [0.035 secs, 9556 KB]
   Test 8: TEST OK [0.035 secs, 10012 KB]
   Test 9: TEST OK [0.036 secs, 10060 KB]
   Test 10: TEST OK [0.039 secs, 10052 KB]
   Test 11: TEST OK [0.042 secs, 10100 KB]

C++ Russ:
   Test 1: TEST OK [0.004 secs, 1356 KB]
   Test 2: TEST OK [0.004 secs, 1344 KB]
   Test 3: TEST OK [0.004 secs, 1364 KB]
   Test 4: TEST OK [0.004 secs, 1344 KB]
   Test 5: TEST OK [0.007 secs, 1384 KB]
   Test 6: TEST OK [0.004 secs, 1364 KB]
   Test 7: TEST OK [0.011 secs, 1352 KB]
   Test 8: TEST OK [0.028 secs, 1356 KB]
   Test 9: TEST OK [0.052 secs, 1360 KB]
   Test 10: TEST OK [0.088 secs, 1344 KB]
   Test 11: TEST OK [0.235 secs, 1348 KB]

Java Russ:
   Test 1: TEST OK [0.117 secs, 23400 KB]
   Test 2: TEST OK [0.110 secs, 23616 KB]
   Test 3: TEST OK [0.110 secs, 23704 KB]
   Test 4: TEST OK [0.112 secs, 23284 KB]
   Test 5: TEST OK [0.131 secs, 23920 KB]
   Test 6: TEST OK [0.210 secs, 23772 KB]
   Test 7: TEST OK [0.145 secs, 23880 KB]
   Test 8: TEST OK [0.243 secs, 28052 KB]
   Test 9: TEST OK [0.373 secs, 30576 KB]
   Test 10: TEST OK [0.495 secs, 32148 KB]
   Test 11: TEST OK [0.618 secs, 46160 KB]

'''

# N <= 160, gcd <= 80
prime12 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]

class Ari:
    def prog(self, N):
        ans = [(0, 0, 1), (1, 1, 1)]
        for denom in range(2, N + 1):
            ans.append((1/denom, 1, denom))

        for nom in range(2, N):
            for denom in range(nom+1, N+1):
                if denom % nom != 0:
                    gcd = 1
                    for divisor in prime12:
                        if divisor >= nom: break
                        elif denom % divisor == 0 and nom % divisor == 0:
                            gcd = divisor
                            continue
                    if gcd == 1:
                        ans.append((nom/denom, nom, denom))

        return sorted(ans)

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase()
    a = Ari()

    print(list(map(lambda x : '{}/{}'.format(x[1], x[2]), a.prog(5))))
    t.assertCountEqual(['0/1', '1/5', '1/4', '1/3', '2/5', '1/2', '3/5', '2/3', '3/4', '4/5', '1/1'],
                       list(map(lambda x : '{}/{}'.format(x[1], x[2]), a.prog(5))) )

    print(list(map(lambda x : '{}/{}'.format(x[1], x[2]), a.prog(6))))
    t.assertCountEqual(['0/1', '1/6', '1/5', '1/4', '1/3', '2/5', '1/2', '3/5', '2/3', '3/4', '4/5', '5/6', '1/1'],
                       list(map(lambda x : '{}/{}'.format(x[1], x[2]), a.prog(6))) )
    print('OK!')

else:
    def outputLines(intArr2: List[List[int]]) -> int:
        f = open('frac1.out', 'w')
        for s in intArr2:
            f.write('{}/{}\n'.format(s[1], s[2]))
        f.close()
        return len(intArr2)

    g = Ari()
    fin = open('frac1.in', 'r')
    l = fin.readlines()
    fin.close()
    N = int(l[0])

    ans = g.prog(N)
    outputLines(ans)
