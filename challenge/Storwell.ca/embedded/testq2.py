import subprocess
from unittest import TestCase

if __name__ == '__main__':
	with open('inputs.q2') as f:
		t = TestCase()
		for ln in f.readlines():
			lnss = ln.split()
			b62 = subprocess.check_output(['./a.out', lnss[0]]).decode().strip()
			print(lnss[0], b62)
			t.assertEqual(lnss[1], b62)
