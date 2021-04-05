def q6():
    a = [0] * 26
    for i in range( 2, 26 ):
        a[i] = i
    print(0, a)

    for k in range( 2, 26 ):
        if a[k] != 0:
            for j in range( 2*k, 26, k ):
                a[j] = 0
            print(k, a)

    s = 0
    for i in range(26):
        if a[i] > 0:
            s += 1
    print(s)

q6()
