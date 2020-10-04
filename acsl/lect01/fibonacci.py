
def addTo(m, fb):
    fb[m] = fb[m - 1] + fb[m - 2]

def main():
    a = None
    n = input("N = ")
    n = int(n)
    if n > 0:
        a = [0] * n # a quick way to initialize a list of sice n
        # n = 5
        # [0, 0, 0, 0, 0]

    if n < 2:
        print(1)
        return

    a[0] = 1
    a[1] = 1
    # [1, 1, 0, 0, 0]

    for x in range(2, n): # 2, 3, ... 4 (if n = 5)
        # x = 2, x = 3, x = 4
        # put a(x) = a(x-1) + a(x-2) 
        addTo(x, a)

    print(a[n-1])

main()

