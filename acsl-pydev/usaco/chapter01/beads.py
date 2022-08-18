'''
ID: odys.zh1
LANG: PYTHON3
TASK: beads
'''
from typing import List

class Beads:
    def breakBeads(self, datalines: List[str]) -> int:
        n = int(datalines[0])
        beads = datalines[1].strip()

        # pad first to last
        b0 = beads[0]
        i = 0
        while i < n and (beads[i] == b0 or beads[i] == 'w' or b0 == 'w'):
            beads += beads[i]
            if b0 == 'w':
                b0 = beads[i]
            i += 1
        
        b0 = beads[0] # current state
        n = len(beads)
        maxl = 1
        lenw = 1 if b0 == 'w' else 0
        lenl, lenr = 0, 1
        for i in range(1, n):
            if beads[i] == 'w':
                lenw += 1
                maxl = max(lenr + lenl + lenw, maxl)
            else: # state is not w
                if b0 == 'w':
                    b0 = beads[i]
                    lenw += 1
                elif beads[i] == b0:
                    # keep going
                    lenr += 1 + lenw
                    lenw = 0
                    maxl = max(lenr + lenl, maxl)
                else:
                    # switch state
                    b0 = beads[i]
                    # count middle w into right, always makes max to be used in the future
                    lenl, lenr = lenr, 1 + lenw
                    lenw = 0
                    maxl = max(lenr + lenl, maxl)
        return min(maxl, int(datalines[0]))


def outputLines(intArr2: List[str]) -> int:
    f = open('beads.out', 'w')
    for s in intArr2:
        f.write(str(s) + '\n')
    f.close()
    return len(intArr2)
 
if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    g = Beads() 

    t.assertEqual(8, g.breakBeads(['11', 'rwrwbwrwbwr']))
    t.assertEqual(5, g.breakBeads(['7',  'rwbrbwr']))

    # 0         5     8 9 10 11  13 14 15 16          22 23        28
    # w w w b b r w r b r b  r r b  r  b  r w r w w r b  w r w r r b
    t.assertEqual(11, g.breakBeads(open("beads.in").readlines()))

    t.assertEqual(3, g.breakBeads(['3', 'rrr']))
    t.assertEqual(5, g.breakBeads(['5', 'rrrbb']))
    t.assertEqual(7, g.breakBeads(['7', 'rrrwbbw']))
    t.assertEqual(5, g.breakBeads(['5', 'rrrww']))
    t.assertEqual(2, g.breakBeads(['2', 'rb']))
    t.assertEqual(5, g.breakBeads(['7', 'rbrwbwb']))
    t.assertEqual(6, g.breakBeads(['8', 'rbrwbwbw']))
    t.assertEqual(20, g.breakBeads(['22', 'rbwrwrwbwbwbwbwbwbwbwb']))
    #                                                              bwrwb
    t.assertEqual(9, g.breakBeads(['50', 'bbrrrbrrrrrrrrbrbbbrbrrbrrrrbbbrbrbbbbbrbrrrbbrbbb']))
    t.assertEqual(74, g.breakBeads(['77', 'rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr']))
    print('OK!')

else:
    g = Beads()
    fin = open('beads.in', 'r')
    ans = g.breakBeads(fin.readlines()) 
    fin.close()
    outputLines([ans])
