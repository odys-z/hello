'''
ID: odys.zh1
LANG: PYTHON3
TASK: skidesign
'''

def redesign(lines):
    def stat(heights, mid):
        s = 0

        for h in heights:
            d = h - mid
            if d < -8:
                s += (d + 8) ** 2
            elif d > 9:
                s += (d - 9) ** 2
        return s

    hills = [int(l.strip()) for l in lines]
    hills.sort()

    center = (hills[0] + hills[-1]) // 2
    cost = stat(hills, center)
    
    d = 1
    center += d
    cost_ = stat(hills, center)
    
    if cost_ > cost:
        d = -1
        cost_, cost, center = cost, cost_, center - 1
    
    while cost_ < cost:
        cost = cost_ 
        center += d
        print(cost_)
        cost_ = stat(hills, center)

    # cost = float('inf')
    # for x in range(9, 91):
    #     print(x, '\t', stat(hills, x))
    #     cost = min(stat(hills, x), cost)
    
    # print(cost)

    return cost

def outputLines(intArr2: int) -> int:
    f = open('skidesign.out', 'w')
    f.write(str(intArr2) + '\n')
    f.close()
    return intArr2
 
# fin = open('skidesign3.in', 'r') # 18
# fin = open('skidesign2.in', 'r')  # 22946
# fin = open('skidesign.in', 'r')  # 42940
fin = open('skidesign.in', 'r')  # 395875 
N = fin.readline()
lines = fin.readlines()
fin.close()

# lines = ['0', '18'] # 1
# lines = ['0', '18', '5', '17', '18'] # 1
outputLines(redesign(lines))
