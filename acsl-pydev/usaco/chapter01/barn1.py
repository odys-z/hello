'''
ID: odys.zh1
LANG: PYTHON3
TASK: barn1
'''
from typing import List
import heapq

def barn1 (maxB: int, stalls: int, cnts: int, nums: List[str]) -> int:
    costs, buys = [], []
    heapq.heapify(costs)

    for i in range(len(nums)):
        nums[i] = int(nums[i].strip())
    
    nums.sort()
    print(nums)

    prevn = -1
    prevlen = 0
    for n in nums:
        if prevlen > 0 and prevn + 1 != n:
            dist = n - prevn - 1
            heapq.heappush(costs, (dist, dist / prevlen, buys[-1][0], n)) # cost, price, prev buying, next buying
            prevn = n
            prevlen = 1
            buys.append([n, n])
        else:
            prevlen += 1
            prevn = n
            if len(buys) > 0:
                buys[-1][1] = n
            else: # first buy
                buys.append([n, n])

    print(costs)
    totalCost = 0
    for buy in buys:
        totalCost += buy[1] - buy[0] + 1

    # costs of merging
    while len(costs) + 1 > maxB:
        cost, price, prv, nxt = heapq.heappop(costs)
        print(cost, price, prv, nxt)
        totalCost += cost

    print(totalCost)
    return totalCost

fin = open('barn1.in', 'r')
[M, S, C] = fin.readline().split()
r = barn1(int(M), int(S), int(C), fin.readlines())
fin.close()

fout = open('barn1.out', 'w')
fout.write(str(r) + '\n')
fout.close()
