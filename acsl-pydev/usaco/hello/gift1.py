"""
ID: odys.zh1
LANG: PYTHON3
TASK: gift1
"""

class GiftGame:
    '''
    https://train.usaco.org/usacoprob2?a=EaNFNvaYCjT&S=ride
    '''
    def gift(self, indat):
        def give(bank, amt, names):
            for n in names:
                balance = bank[n] + amt
                bank.update({n: balance}) 

        bank = {}

        np = int(indat[0])
        for p in range(1, np + 1):
            name = indat[p]
            bank.update({name: 0})
        
        rnd = np + 1
        while rnd < len(indat):
            name = indat[rnd]
            amt = indat[rnd + 1].strip().split()
            recievers = int(amt[1])
            rnd += 2
            if recievers > 0:
                eachAmt = int(amt[0]) // recievers
                balance = bank[name] - eachAmt * recievers
                bank.update({name: balance})

                give(bank, eachAmt, indat[rnd : rnd + recievers])
                rnd += recievers
        
        res = []
        for p in bank: 
            v = bank[p]
            res.append("{} {}".format(p.strip(), v))

        return res

def outputLines(ss):
    f = open('gift1.out', 'w')
    for s in ss:
        f.write(s + '\n')
    f.close()
        
if __name__ == 'gift1':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    g = GiftGame()
    t.assertCountEqual(["dave 302", "laura 66", "owen -359", "vick 141", "amr -150"],
                       g.gift(open("gift1_1.in").readlines()))
else:
    g = GiftGame()
    fin = open('gift1.in', 'r')
    ans = g.gift(fin.readlines()) 
    fin.close()
    outputLines(ans)

print('OK!')