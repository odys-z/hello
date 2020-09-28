
def add2(n, fseq):
    print('add2({})'.format(n))
    fseq[n] = fseq[n - 1] + fseq[n - 2]

def main():
    a = None
    n = input("N = ")
    n = int(n)
    if n > 0:
        a = [0] * n # a quick way to initialize a list of sice n
    if n < 2:
        print(1)
        return

    a[0] = 1
    a[1] = 1

    for x in range(2, n): # 2, 3, ... 4 (if N = 5)
        add2(x, a);

    print(a[n-1])

main()
