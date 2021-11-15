'''
ID: odys.zh1
LANG: PYTHON3
TASK: namenum
'''
from typing import List
from unittest import TestCase

'''
    This is a failed example for wrong data structure -
    path and leaf can not differentiated by dict{}.
'''
def findName(nums) -> List[str]:
    # 2: A,B,C     5: J,K,L    8: T,U,V      3: D,E,F     6: M,N,O    9: W,X,Y     4: G,H,I     7: P,R,S
    dial = {}
    dial.update({'2': ['A', 'B', 'C']})
    dial.update({'5': ['J', 'K', 'L']})
    dial.update({'8': ['T', 'U', 'V']})
    dial.update({'3': ['D', 'E', 'F']})
    dial.update({'6': ['M', 'N', 'O']})
    dial.update({'9': ['W', 'X', 'Y']})
    dial.update({'4': ['G', 'H', 'I']})
    dial.update({'7': ['P', 'R', 'S']})

    def putTo(dictions : [List[int]], word : str):
        '''
            XQ WB
            {U: Q, W: B}
            AXQ AWB
            {A: {U: Q, W: B}}
        '''
        if len(word) > 1:
            d = dictions.get(word[0])
            if d == None:
                d = dict()
                dictions.update({word[0]: d})
            putTo(d, word[1:])
        else:
            dictions.update({word[0]: None})

    dct = dict()
    fin = open('dict.txt')
    ln = fin.readline().strip()
    while len(ln) > 0:
        putTo(dct, ln)
        ln = fin.readline().strip()
    fin.close()
    
    res = []
    
    def dfs(path, nums, dcts):
        for n in dial.get(nums[0]):
            w = dcts.get(n)
            if w is not None:
                if len(nums) > 1:
                    dfs(path + n, nums[1:], w)
                else:
                    res.append(path + n)

            '''
            failed: every n are added here
            elif len(nums) == 1:
                res.append(path + n)
            '''

    dfs('', nums, dct)

    return res

def outputLines(res: List[str]):
#     print(res)
    f = open('namenum.out', 'w')
    if res != None and len(res) > 0:
        for rl in res:
            f.write(rl + '\n')
    else:
        f.write('NONE\n')
    f.close()

if __name__ == "__main__": # PyUnit
    fin = open('namenum.in')
    nums = fin.readline().strip()
    fin.close()

    ans = findName(nums)
    outputLines(ans)
else:
    ans = findName('4734')
    TestCase().assertCountEqual(['GREG'], ans)
    ans = findName('223')
    TestCase().assertCountEqual(['ABE', 'ACE'], ans)
    ans = findName('5747867437')
    TestCase().assertCountEqual(['KRISTOPHER'], ans)

print('ok')
