from inter import sum8

def printOctal(s, d, r):
	s = int(s, 8)
	d = int(d, 8)
	r = int(r)

	width = s + r * (r - 1) // 2 * d
	width = len('{}'.format(width))
	templOct = '{:%do}' % width
	dwidth = len('{:o}'.format(d))
	templ8 = '{:%do} ({:%dd})' % (width, dwidth + 1)
	dwidth = len('{:d}'.format(d))
	templ10_p = '{:%dd} ({:%dd})' % (width, dwidth + 1)
	templ10_0 = '{:%dd}     ' % width

	# print triangle
	print('\ns={}, d={}, r={}, numeral octal triangle:'.format(s, d, r), end='')
	n = s - d
	for rx in range(r + 1):
		print('r={:2d}:  '.format(rx), end='')
		for dx in range(rx):
			n += d
			print(templOct.format(n), end='  ')
		print('')

	digsum, deltasum, digsum_1 = 0, 0, 0
	# print digits sum
	print('\ndigits sum in octal:', end='')
	n = s - d
	for rx in range(r + 1):
		print('r={:2d}:  '.format(rx), end='')
		for dx in range(rx):
			n += d
			digsum_1, digsum = digsum, sum8(n)
			deltasum = digsum - digsum_1
			print(templ8.format(digsum, deltasum), end='  ')
		print('')

	print('\ndigits sum in decimal:', end='')
	n = s - d
	for rx in range(r + 1):
		print('r={:2d}:  '.format(rx), end='')
		for dx in range(rx):
			n += d
			digsum_1, digsum = digsum, sum8(n)
			deltasum = digsum - digsum_1
			print(templ10_p.format(digsum, deltasum), end='  ')
		print('')


	print('\ns_i - sum(digits):', end='')
	n = s - d
	digsum, deltasum, digsum_1 = 0, 0, 0
	for rx in range(r + 1):
		print('r={:2d}:  '.format(rx), end='')
		for dx in range(rx):
			n += d
			digsum_1, digsum = digsum, n - sum8(n)
			deltasum = digsum - digsum_1
			print((templ10_p if deltasum != 0 else templ10_0)
				.format(digsum, deltasum), end='  ')
		print('')


printOctal('0', '1', '5')

printOctal('0', '1', '18')
printOctal('0', '2', '12')
printOctal('0', '3', '12')
