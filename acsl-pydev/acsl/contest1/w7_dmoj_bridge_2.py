import sys

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
        bider = int(rec[0]) - 1
        operx = ( bider + 1 ) % 2 # oper = 0 if rec[0] == 1 else 1

        bid = int(rec[1])
        win = int(rec[2])
        if bid + 6 <= win:
            # win
            teams[bider] = 100 # vulnerable
            scr[bider * 2] += underScore(bid, rec[3])
            scr[bider * 2 + 1] += overScore(win - bid - 6, rec[3])
            winner = bider
        else: # lose
            penalty = teams[ operx ]
            scr[operx * 2 + 1] += penalty * bid
            winner = operx
        
        if scr[winner * 2] >= 100:
            restart = True
        scors[i] = scr.copy()

    return scors

# s = sys.stdin.read().split()
# s = '1 2 8 C 1 1 9 H 2 4 10 H 2 2 11 T 2 3 6 S'.split()
s = '1 2 8 H 2 3 10 S 1 1 8 T 2 5 8 C 1 5 12 D'.split()

dat = list()
for x in range(0, len(s), 4):
    dat.append( s[x : x+4] )
asw = bridge2009(dat)

for i in range(len(asw)):
#     print( '{}\n{}\n{}\n{}'.format(*asw[i]) )
#     print( '1. {} {} {} {}'.format(*asw[i]) )
    print( *asw[i] )