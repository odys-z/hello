def fn(n, b):
    print(b)
    print(n)
    b[n] = n * b[n-1]

def main():
    b = None
    n = input("N=")
    n = int(n)
    if n > 0:
        b = [0] * n

    if n < 2:
        print(1)
        return

    b[0] = 1
    b[1] = 1

    for n in range(2, n):
        fn(n, b)

    print(b[n])

main()

