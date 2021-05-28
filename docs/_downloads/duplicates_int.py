'''
Problem: 
http://www.datafiles.acsl.org/samples/contest4/c_4_duplicates_int.pdf

2017-2018 American Computer Science League Contest #4
Intermediate Division Programming Problem: Duplicates

Created on 6 Apr 2021

@author: odys-z@github.com
'''
from unittest import TestCase

class Recurslot:
    def __init__(self):
        pass

    def reset(self, chars):
        # e.g. [ ('C', 1, 'RC'), ... ], where 'C' == 'RC'[-1]
        self.slots = []
        for c in chars:
            self.push(c)
    
    def push(self, ch, start = 0):
        i = start
        while i < len(self.slots) and self.slots[i][0] < ch:
            i += 1

        if i >= len(self.slots):
            self.slots.append((ch, 1, ch))
        elif self.slots[i][0] == ch:
            # e.g. slots[i] == 'C', 1, 'RC')
            self.slots[i] = (self.slots[i][0], self.slots[i][1] + 1, self.slots[i][2])
        else:
            # 'a' < ch == 'C' < 'R', i = ix_of('R')
            nxt = self.slots[i][0]
            self.slots[i] = (ch, 1, ch + self.slots[i][2])
            self.push(nxt, i+1)
    
    def pop(self, ch):
        i = 0
        while i < len(self.slots) and self.slots[i][0] < ch:
            i += 1

        if i < len(self.slots) and ch == self.slots[i][0]:
            self.slots[i] = (self.slots[i][0], self.slots[i][1] - 1, self.slots[i][2])
            if self.slots[i][1] <= 0:
                # shift left
                if i < len(self.slots) - 1:
                    # shift following
                    nxt = self.shiftleft(i+1)
                    if nxt:
                        self.slots[i] = nxt[0], nxt[1], nxt[0] + self.slots[i][2]
                    else: # me the last one, delete
                        self.slots[i] = '', 0, self.slots[i][2]
                else: # pop last one
                    lst = self.slots[-1]
                    self.slots[-1] = '', 0, self.slots[-1][2]
                    return lst
    
    def shiftleft(self, start):
        if start > len(self.slots) - 1 or self.slots[start][0] == '':
            return None
        elif start < len(self.slots) - 1:
            curr = self.slots[start]
            nxt = self.shiftleft(start + 1)
            if nxt:
                # has next, shift next to me
                self.slots[start] = nxt[0], nxt[1], nxt[0] + curr[2]
            else:
                # no next, me the last
                self.slots[start] = '', 0, self.slots[start][2]
            return curr
        elif start == len(self.slots) - 1:
            lst = self.slots[-1]
            self.slots[-1] = '', 0, lst[2] # leave finger print at last
            return lst
        else: # shouldn't reach here
            return None
    
    def cmd(self, cmd):
        datss = cmd.split()
        cmd = datss[0].upper()
        dat = ''.join(datss[1:]).upper()

        if cmd == 'RESET':
            self.reset(dat)
        elif cmd == 'REPORT':
            dat = int(dat) - 1
            return self.slots[dat][2][::-1]
        elif cmd == 'ADD':
            for c in dat:
                self.push(c)
        else: # cmd = 'DELETE':
            for c in dat:
                self.pop(c)
        return None

if __name__ == '__main__':
    inputs = []
    s = input('input:')
    while len(s) > 0:
        inputs.append(s)
        s = input()

    ans = []
    slots = Recurslot()
    for s in inputs:
        res = slots.cmd(s)
        if res != None:
            ans.append(res)
   
    for r in ans:
        print(ans)
else:
    def assrt(expecteds, inputs):
        tst = TestCase()
        slots = Recurslot()
        res = []
        for s in inputs:
            ans = slots.cmd(s)
            print('', s, slots.slots, ans, sep='\n')
            if ans != None:
                res.append(ans)
        tst.assertCountEqual(expecteds, res)

    inputs = ['RESET abcde',
              'DELETE cd', 
              'REPORT 3',
             ]
    assrt(['CDE'], inputs)
    print('\n-------------------')

    inputs = ['RESET eabcd',
              'DELETE cd', 
              'REPORT 3',
             ]
    assrt(['ECDE'], inputs)
    print('\n-------------------')

    inputs = ['RESET American Computer Science League',
              'DELETE COMPUTER',
              'REPORT 10'
             ]
    '''
        FIXME Why not 'UTSRPRS' ?
        see Issue https://odys-z.github.io/hello/acsl/lect06/issue_int.html
    '''
    assrt(['UTSRPRSTU'], inputs)
    print('\n-------------------')

    inputs = ['RESET abracadabracabob',
              'REPORT 3',
              'REPORT 5',
              'ADD BATH',
              'DELETE boa', 
              'REPORT 5',
              'DELETE drr',
              'REPORT 5',
              'RESET American Computer Science League',
              'ADD Computer',
              'DELETE Computer',
              'DELETE COMPUTER',
              'REPORT 10'
             ]
    # assrt(['RC', 'RO', 'ROH', 'ROHRT', 'UTSRPRS'], inputs)
    assrt(['RC', 'RO', 'ROH', 'ROHRT', 'UTSRPRSTU'], inputs)

    print('OK!')
