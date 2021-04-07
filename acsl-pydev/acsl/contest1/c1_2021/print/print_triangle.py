
import os, sys; sys.path.insert(0, '..')
from inter import sum8

def printOctalRows(cellTempl, s, d, r):
	'''
		params
		======
		cellTempl
		---------
			n: number,
			digsum: digit sum,
			deltasum: sum different to the previous
	'''

	digsum, deltasum, digsum_1 = 0, 0, 0
	# print digits sum
	sbuf = ''
	n = s - d
	for rx in range(r + 1):
		if rx > 0:
			sbuf += '    r={:2d}'.format(rx)

		for _ in range(rx):
			n += d
			digsum_1, digsum = digsum, sum8(n)
			deltasum = digsum - digsum_1
			sbuf += ' & ' + cellTempl.format(n, digsum, deltasum)

		if rx > 0:
			sbuf += '\\\\\n'

	return sbuf

# printOctal('0', '1', '5')
#
# printOctal('0', '1', '18')
# printOctal('0', '2', '12')
# printOctal('0', '3', '12')
