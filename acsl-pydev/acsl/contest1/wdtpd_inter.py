
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

def q10(A):
	'''
		In this program, we use i, j start from 0, step to 4, exclusive, in concordance
		with python - as their values been adjusted when used in computation.
	'''
	s = 0
	for i in range(4):
		for j in range(4):
			A[i][j] = A[i][j] + (i+1) * (j+1) + A[j][i]

	for i in range(4):
		for j in range(4):
			if A[i][j] / 2 != int(A[i][j] /2): A[i][j] = A[i][j] + 1
			if A[i][j] / 2 == int(A[i][j] /2): A[i][j] = A[i][j] // 2 # use // to round float
			if A[i][j] > s: s = A[i][j]
			print(i, j, A)
	print(s)

def q11(a, b, c, d, e):
	'''
		a = 16: b = 2: c = 4: d = 0: e = 5
		if a < b then a = a + b else a = a - b
		if a * d < c * e then a = a + d else c = c + e
		if b ^ d = 1 then d = d + 1 else b = b + 1
		if int(a / c) = a / c then a = a / c else a = a - c
		if (a < e) or (b >= d) then a = e else b = d
		if (b >= c) and (d <= e) then c = b - c else d = a - e
		print a ^ d + b * e / a – c * (a / e + b ^ b)
		end
	'''
	if a < b: a = a + b
	else: a = a - b
	print('1:', a, b, c, d, e)

	if a * d < c * e: a = a + d
	else: c = c + e
	print('2:', a, b, c, d, e)

	if b ** d == 1: d = d + 1
	else: b = b + 1
	print('3:', a, b, c, d, e)

	if int(a / c) == a / c: a = a / c
	else: a = a - c
	print('4:', a, b, c, d, e)

	if (a < e) or (b >= d): a = e
	else: b = d
	print('5:', a, b, c, d, e)

	if (b >= c) and (d <= e): c = b - c
	else: d = a - e
	print('6:', a, b, c, d, e)
	print(a ** d + b * e / a - c * (a / e + b ** b))

def q12(a):
	'''
		s=0
		for i = 1 to 4
		for j = 1 to 4
		a(i,j)=a(i,j)-a(j,i)
		next j
		next i
		for i = 1 to 4
		for j = 1 to 4
		if a(i,j) >= 10 then a(i,j)=a(i,j)-10
		if a(i,j) / 2 = int(a(i,j)/2) then a(i,j) = a(i,j) / 2
		if abs(a(i,j)) < 5 then a(i,j) = 0
		next j
		next i
		for i = 1 to 4
		for j = 1 to 4
		if a(i,j) = 0 then s = s + 1
		next j
		next i
		print s
		end

		a:
		2 6 0 -1
		-3 4 -2 3
		0 3 -1 -4
		8 2 -3 0
		where A(1,2) = 6
	'''
	s = 0
	for i in range(4):
		for j in range(4):
			a[i][j] = a[i][j] - a[j][i]
	print('- -', a)

	for i in range(4):
		for j in range(4):
			if a[i][j] >= 10: a[i][j] = a[i][j] - 10
			if a[i][j] / 2 == int(a[i][j] / 2): a[i][j] = a[i][j] / 2
			if abs(a[i][j]) < 5: a[i][j] = 0
			print(i, j, a)

	for i in range(4):
		for j in range(4):
			if a[i][j] == 0: s = s + 1
	print(s)

q5(10, 5, 20, 1, 2)

print('\nq10:')
q10([[4, 1, 2, 3], [1, 0, 6, 8], [9, 2, 7, 5], [4, 3, 9, 7]])

print('\nq11:')
q11(a = 16, b = 2, c = 4, d = 0, e = 5)

print('\nq12:')
q12([[ 2, 6, 0, -1], [-3, 4, -2, 3], [ 0, 3, -1, -4], [8, 2, -3, 0]])
