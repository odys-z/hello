'''
ID: odys.zh1
LANG: PYTHON3
TASK: lamps
'''

from typing import List

states = [
['111111'],
['000000', '010101', '011011', '101010'],
['000000', '001110', '010101', '100100', '101010', '110001', '111111'],
['000000', '001110', '010101', '011011', '100100', '101010', '110001', '111111']]

class Lookup:
    '''
       Test 1: TEST OK [0.035 secs, 9708 KB]
       Test 2: TEST OK [0.034 secs, 9756 KB]
       Test 3: TEST OK [0.097 secs, 9720 KB]
       Test 4: TEST OK [0.088 secs, 9664 KB]
       Test 5: TEST OK [0.074 secs, 9668 KB]
       Test 6: TEST OK [0.057 secs, 9772 KB]
       Test 7: TEST OK [0.059 secs, 9804 KB]
       Test 8: TEST OK [0.038 secs, 9752 KB]
    '''
    def prog(self, C, ons: List[int], offs: List[int]):

        C = min(C, 3)
        ans = []
        
        def test(v, ons, offs):
            for on in ons:
                if v[on] != '1':
                    return False
            for off in offs:
                if v[off] != '0':
                    return False
            return True
        
        for x in range(len(offs)):
            offs[x] = (int(offs[x]) -1) % 6

        for x in range(len(ons)):
            ons[x] = (int(ons[x]) -1) % 6

        for s in states[C]:
            if test(s, ons, offs):
                ans.append(s)

        return sorted(ans)

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase()
    a = Lookup()

    t.assertCountEqual(['000000', '010101', '011011'],
                       a.prog(1, [], [7]))

    print('OK!')

else:
    def outputLines(intArr2: List[str], N) -> int:
        f = open('lamps.out', 'w')
        if len(intArr2) == 0:
            f.write('IMPOSSIBLE\n')
        else:
            for s in intArr2:
                x = N
                while 0 < x:
                    f.write(s[0: min(x, 6)])
                    x -= 6
                f.write('\n')
        f.close()
        return len(intArr2)

    g = Lookup()
    fin = open('lamps.in', 'r')
    l = fin.readlines()
    fin.close()
    N = int(l[0])
    C = int(l[1])

    ons  = l[2].split()
    ons  = [int(x) for x in ons]
    
    offs = l[3].split()
    offs = [int(x) for x in offs]

    ans = g.prog(C, ons[:-1], offs[: -1])
    outputLines(ans, N)
