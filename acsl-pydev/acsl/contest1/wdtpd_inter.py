
def q5(a, b, c, d, e):
    if a + b > c / e:
        b = a - b
    else:
        c = c * c
    print('1:', a, b, c, d, e)

    if a / b == c / b :
        a = b + 2 * e
    else:
        d = b ** 2
    print('2:', a, b, c, d, e)

    if a > b and c > d :
        e = d / b
    else:
        b = a + c / e
    print('3:', a, b, c, d, e)

    if a + c > d * e or b / c == b / (2 * a):
        b = a - e
    else: c = b - c
    print('4:', a, b, c, d, e)

    if a < b or c < d and b + e == a:
        d = d - c
    else: c = c / a
    print('5:', a, b, c, d, e)

    print('x:', c / ( b + e) - d ** 2 + a / e)

q5(10, 5, 20, 1, 2)

