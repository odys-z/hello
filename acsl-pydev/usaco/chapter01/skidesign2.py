'''
ID: odys.zh1
LANG: PYTHON3
TASK: skidesign
'''

def redesign(lines):
    def stat1(heights, mid):
        s = 0

        for h in heights:
            d = h - mid
            if d < -8:
                s += (d + 8) ** 2
            elif d > 9:
                s += (d - 9) ** 2
        return s

    def stat2(heights, mid):
        s = 0

        for h in heights:
            d = h - mid
            if d < -9:
                s += (d + 9) ** 2
            elif d > 8:
                s += (d - 8) ** 2
        return s


    hills = [int(l.strip()) for l in lines]
    hills.sort()

    # center = (hills[0] + hills[-1]) // 2
    # cost = stat(hills, center)
    
    # d = 1
    # center += d
    # cost_ = stat(hills, center)
    
    # if cost_ > cost:
    #     d = -1
    #     cost_, cost = cost, cost_
    
    # while cost_ < cost:
    #     cost = cost_ 
    #     center += d
    #     cost_ = stat(hills, center)

    cost1, cost2 = float('inf'), float('inf')
    for x in range(8, 92):
        cost1 = min(stat1(hills, x), cost1)
        cost2 = min(stat2(hills, x), cost2)
    
    return min(cost1, cost2)

def outputLines(ss: int) -> int:
    f = open('skidesign.out', 'w')
    f.write(str(ss) + '\n')
    f.close()
    return ss
 
# fin = open('skidesign.in', 'r') # 18
# fin = open('skidesign2.in', 'r')  # 22946
fin = open('skidesign.in', 'r')  # 42940
lines = fin.readlines()
fin.close()

# lines = ['0', '18'] # 1
# lines = ['0', '18', '5', '17', '18'] # 1
outputLines(redesign(lines))
