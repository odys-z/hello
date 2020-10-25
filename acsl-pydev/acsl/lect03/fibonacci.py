import time

'''
def addTo(m, fb):
    fb[m] = fb[m - 1] + fb[m - 2]
'''

def main():
    a = None
    n = input("N = ")
    n = int(n)
    if n > 0 and n >= 2:
        a = [0] * n # a quick way to initialize a list of sice n
        # n = 5
        # [0, 0, 0, 0, 0]

    if n < 2:
        print(1)
        return

    a[0] = 1
    a[1] = 1
    # [1, 1, 0, 0, 0]

    startime = time.time()
    for x in range(2, n): # x = 2, 3, ... 4 (if n = 5)
        # put a(x) = a(x-1) + a(x-2)

        a[x] = a[x-1] + a[x-2]
        # a[x] = x * a[n-1]
        # a[0] = 0! = 1
        # a[1] = 1! = 1
        # a[2] = 2 != 2 = 2 * a[1]
        # a[3] = 3 * a[2]
        x = 3 * x
        x *= 3
        # ...
        # addTo(x, a)

    endtime = time.time()
    print(endtime - startime)
    print(a)

main()
