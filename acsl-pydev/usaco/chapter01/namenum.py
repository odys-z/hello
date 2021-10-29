'''
ID: odys.zh1
LANG: PYTHON3
TASK: namenum
'''
from typing import List

# 2: A,B,C     5: J,K,L    8: T,U,V      3: D,E,F     6: M,N,O    9: W,X,Y     4: G,H,I     7: P,R,S
dial = [None] * 10
dial[2] = ['A', 'B', 'C']
dial[5] = ['J', 'K', 'L']
dial[8] = ['T', 'U', 'V']
dial[3] = ['D', 'E', 'F']
dial[6] = ['M', 'N', 'O']
dial[9] = ['W', 'X', 'Y']
dial[4] = ['G', 'H', 'I']
dial[7] = ['P', 'R', 'S']

def findName(num: str) -> List[str]:
    global dail

    names = dial[int(num[0])]

    for n in num[1:]:
        names2 = []
        for name in names:
            for dialname in dial[int(n)]:
                names2.append(name + dialname)
        names = names2

    names = set(names)

    lines = []
    # fin = open('namenumdict.txt')
    fin = open('dict.txt')
    ln = fin.readline().strip()
    while len(ln) > 0:
        if ln in names:
            lines.append(ln)
        ln = fin.readline().strip()
    fin.close()
    return lines

def brutal(num):
    global dial

    permus, temp = set(), set()
    for n in dial[int(num[0])]:
        permus.add(n)

    for n in num[1:]:
        tails = dial[int(n)]
        for p in permus:
            for t in tails:
                temp.add(p + t)
        permus, temp = temp, set()
    
    fin = open('dict.txt')
    ln = fin.readline().strip()
    lines = []
    while len(ln) > 0:
        if ln in permus:
            lines.append(ln)
        ln = fin.readline().strip()
    fin.close()
    return lines

def outputLines(res: List[str]):
    print(res)
    f = open('namenum.out', 'w')
    if res != None and len(res) > 0:
        for rl in res:
            f.write(rl + '\n')
    else:
        f.write('NONE\n')
    f.close()

def readnum():
    fin = open('namenum.in')
    num = fin.readline().strip()
    fin.close()
    return num

# ans = findName(readnum())
# print(ans)
ans = brutal(readnum())
outputLines(ans)

