def q1(A, B, C, D, E):
    '''
        A = 2: B = 4: C = 1: D = 3: E = 5
        IF A * D >= B * E THEN A = D ELSE B = E
        IF B – C < E – D THEN C = C + A ELSE D = D + E
        IF A * B + C = B * D + E THEN E = A + B ELSE A = D + E
        IF A ↑ B > C ↑ D THEN E = E + A ELSE E = E + B
        IF ((A < B) AND (C < D)) THEN B = D ELSE A = D
        IF B/2 = INT(B/2) THEN B = B / 2 ELSE B = B + 1
        IF ((A+C > D) OR (B+C < E)) THEN A = C + D ELSE B = A + E
        PRINT A * B + C * D - E
    '''
    if A * D >= B * E: A = D
    else: B = E

    if B - C < E - D: C = C + A
    else: D = D + E

    if A * B + C == B * D + E: E = A + B
    else: A = D + E

    if A ** B > C ** D: E = E + A
    else: E = E + B

    if ((A < B) and (C < D)): B = D
    else: A = D

    if B/2 == int(B/2): B = B / 2
    else: B = B + 1

    if ((A+C > D) or (B+C < E)): A = C + D
    else: B = A + E
    print( A * B + C * D - E )

def q2():
    S=0
    for I in range(1, 13, 1):
        for J in range(1, int(I ** 0.5 + 1), 1):
            if I/J == int(I/J):
                S=S+1
                print('I {},  J {},  S {}'.format(I, J, S))
    print(S)

def q3(a, b, c, d):
    '''
        A = 2: B = 10: C = 5: D = 20
        IF A * B = D THEN A = 2 * A ELSE B = 2*B
        C=C+1
        IF B * C > A * D THEN B = B + 2 ELSE C = C – 2
        D=B–A
        IF B/A > D/C THEN D = 3 + A ELSE A = 4 * A
        IF B^C > 0 THEN B = B – 4
        IF ((A>B) AND (C>D)) THEN C = C + D
        D=D–A
        IF ((A<D) OR (C>B)) THEN D = D – 1 ELSE D = D + 1
        PRINT A*B/(C+D)
    '''
    if a * b == d: a = 2 * a
    else: b = 2*b

    c=c+1
    if b * c > a * d: b = b + 2
    else: c = c - 2

    d = b - a
    if b/a > d/c: d = 3 + a
    else: a = 4 * a

    if b^c > 0: b = b - 4

    if ((a>b) and (c>d)): c = c + d

    d=d-a
    if ((a<d) or (c>b)): d = d - 1
    else: d = d + 1

    print(a*b/(c+d))

def q5(a, b, c, d, e):
    if a + b > c / e: b = a - b
    else: c = c * c
    print('1:', a, b, c, d, e)

    if a / b == c / b: a = b + 2 * e
    else: d = b ** 2
    print('2:', a, b, c, d, e)

    if a > b and c > d: e = d / b
    else: b = a + c / e
    print('3:', a, b, c, d, e)

    if a + c > d * e or b / c == b / (2 * a): b = a - e
    else: c = b - c
    print('4:', a, b, c, d, e)

    if a < b or c < d and b + e == a: d = d - c
    else: c = c / a
    print('5:', a, b, c, d, e)

    print('x:', c / ( b + e) - d ** 2 + a / e)

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

def q7(a, b, c, d, e):
    '''
        a = 10 : b = 8 : c=2 : d=-1 : e=0
        if (a+2)/(b-2)= c then a = a + b
        if a + c - 8 < e then c = c + b else e = e + b
        if b*c > d^2*e/b then d = d * c else d = d * d
        if a + c + d = b + e then c = a - d else b = a + b / 2
        if e - d != a + c then e = e / c else c = c ^ e
        if (a>b) and (b>c) then a = b - c
        if c / 2 = int (c / 2) then c = c / 2
        print (b + d) / e + ( a + e) / b + c
        end
    '''
    if (a + 2) / (b - 2) == c: a = a + b
    print('\n1:', a, b, c, d, e)

    if a + c - 8 < e: c = c + b
    else: e = e + b
    print('2:', a, b, c, d, e)

    if b * c > d ** 2 * e / b: d = d * c
    else: d = d * d
    print('3:', a, b, c, d, e)
    
    if a + c + d == b + e: c = a - d
    else: b = a + b / 2
    print('4:', a, b, c, d, e)

    if e - d != a + c: e = e / c
    else: c = c ^ e
    print('5:', a, b, c, d, e)

    if (a>b) and (b>c): a = b - c
    print('6:', a, b, c, d, e)

    if c / 2 == int (c / 2): c = c / 2
    print('7:', a, b, c, d, e)

    print( (b + d) / e + ( a + e) / b + c )

def q8():
    '''
    for a = 1 to 4
    for b = 1 to 4
    c(a,b)=a*b-2*a
    next b
    next a
    for a = 1 to 4
    for b = 1 to 4
    if c(a,b)<0 then c(a,b)=0
    if c(a,b)/2=int(c(a,b)/2) then c(a,b)=c(a,b)/2
    if c(a,b) < 3 then c(a,b) = 0
    '''
    c = [[0] * 5] * 5
    for a in range(1, 5):
        for b in range( 1, 5 ):
            c[a][b] = a*b - 2*a

    print(c)
    for a in range(1, 5):
        for b in range( 1, 5 ):
            if c[a][b] < 0: c[a][b] = 0
            if c[a][b] / 2 == int(c[a][b]/2): c[a][b]=c[a][b]/2
            if c[a][b] < 3: c[a][b] = 0
            print(a, b, c)
    
    s = 0 
    print(c)
    for a in range(1, 5):
        for b in range( 1, 5 ):
            if c[a][b] != 0:
                s += 1
    print(s)

print('\nq1')
q1( A = 2, B = 4, C = 1, D = 3, E = 5 )

print('\nq2')
q2()

print('\nq3')
q3(2, 10, 5, 20)

print('\nq5')
q5(10, 5, 20, 1, 2)

print('\nq6')
q6()

print('\nq7')
q7(10, 8, 2, -1, 0)

print('\nq8')
q8()
