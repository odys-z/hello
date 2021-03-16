"""
ID: odys.zh1
LANG: PYTHON3
TASK: ride
"""

class Ride:
    '''
    https://train.usaco.org/usacoprob2?a=EaNFNvaYCjT&S=ride
    '''
    def isgo(self, indat):
        def m47(s: str) -> int:
            c47 = 1
            a0 = ord('A') - 1
            for c in s:
                c47 *= ord(c) - a0
            return c47%47 

        commet = indat[0]
        grp = indat[1] 
        c47 = m47(commet.strip())
        g47 = m47(grp.strip())
        if c47 == g47:
            return 'GO'
        else : return 'STAY'

r = Ride()
fin = open('ride.in', 'r')
ans = r.isgo(fin.readlines()) 
fo = open('ride.out', 'w')
fo.write(ans + '\n')
fo.close()
print(ans)
print('OK!')