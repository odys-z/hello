'''
    https://dmoj.ca/problem/acslbridgesr
    <a href='https://dmoj.ca/problem/acslbridgesr/pdf'>View as PDF</a>
    American Computer Science League, 2008/09 Contest #1
    
    github: demoj
    https://github.com/DMOJ/online-judge/blob/master/README.md
'''
from unittest import TestCase

def underScore(triks, suit):
    if suit == 'T':
        return 40 + 30 * (triks - 1)
    elif suit == 'H' or suit == 'S':
        return triks * 30
    else:
        return triks * 20

def overScore(overs, suit):
    if suit == 'C' or suit == 'D':
        return overs * 20
    else: return overs * 30


def bridge2009(records):
    scors = [[0] * 4] * len(records)
    teams = [50, 50] # both not vulnerable at first
    restart = False

    for i in range( len(records) ):
        rec = records[i]
        if i > 0:
            scr = scors[i - 1].copy()
        else: scr = [0] * 4

        if restart:
            scr[0], scr[2] = 0, 0
        restart = False
            
        winner = None
        bider = rec[0] - 1
        operx = ( bider + 1 ) % 2 # oper = 0 if rec[0] == 1 else 1

        if rec[1] + 6 <= rec[2]:
            # win
            teams[bider] = 100 # vulnerable
            scr[bider * 2] += underScore(rec[1], rec[3])
            scr[bider * 2 + 1] += overScore(rec[2] - rec[1] - 6, rec[3])
            winner = bider
        else: # lose
            penalty = teams[ operx ]
            scr[operx * 2 + 1] += penalty * rec[1]
            winner = operx
        
        if scr[winner * 2] >= 100:
            restart = True
        scors[i] = scr.copy()

    return scors

t = TestCase()
r = bridge2009([[1, 2, 8, 'C'], [1, 1, 9, 'H'], [2, 4, 10, 'H'], [2, 2, 11, 'T'], [2, 3, 6, 'S']])
t.assertEqual( [40, 0, 0, 0,], r[0] )
t.assertEqual( [70, 60, 0, 0], r[1] )
t.assertEqual( [70, 60, 120, 0], r[2] )
t.assertEqual( [0, 60, 70, 90], r[3] )
t.assertEqual( [0, 360, 70, 90], r[4] )
print('OK!')
