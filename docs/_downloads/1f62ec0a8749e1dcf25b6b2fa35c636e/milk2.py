'''
ID: odys.zh1
LANG: PYTHON3
TASK: milk2
'''

# https://train.usaco.org/usacoprob2?a=ksu2wlLybOe&S=milk2
class Milk2:
    def milk(self, intvals):
        intv = []
        for l in intvals[1:]:
            ss = l.split()
            intv.append((int(ss[0]), int(ss[1])))

        intv.sort()
        s, e = intv[0]
        
        maxWaiting, maxMilking = 0, e - s
        # Milking from time 1 through 10, then from time 11 through 20 counts as two different time intervals.
        for si, ei in intv[1:]: 
            if e >= si:
                maxMilking = max(ei - s, maxMilking)
                e = max(ei, e)
            else:
                maxMilking = max(e - s, maxMilking)
                maxWaiting = max(si - e, maxWaiting)
                s = si
                e = max(ei, e)
        
        maxMilking = max(e - s, maxMilking)

        return ' '.join([str(maxMilking), str(maxWaiting)])


if __name__ == '__main__':
    pass

def outputLines(res: str):
    f = open('milk2.out', 'w')
    for rl in res:
        f.write(rl + '\n')
    f.close()
 
if __name__ != '__main__':
    from unittest import TestCase

    t = TestCase() 
    m = Milk2() 

    t.assertEqual("900 300", m.milk(['3', '300 1000', '700 1200', '1500 2100']))
    t.assertEqual("100 0", m.milk(['1', '100 200']))
    t.assertEqual("100 1", m.milk(['4', '100 200', '201 301', '302 402', '403 503']))
    t.assertEqual("19 0", m.milk(['10', '2 3', '4 5', '6 7', '8 9', '10 11', '12 13', '14 15', '16 17', '18 19', '1 20']))
    t.assertEqual("1550 100", m.milk(['6', '100 200', '200 400', '400 800', '800 1600', '50 100', '1700 3200']))


else:
    g = Milk2()
    fin = open('milk2.in', 'r')
    ans = g.milk(fin.readlines()) 
    fin.close()
    outputLines([ans])
