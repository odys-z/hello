"""
ID: your_id_here
LANG: PYTHON3
TASK: test
"""
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
x,y = map(int, fin.readline().split())
sum = x+y
fout.print (str(sum) + '\n')
fout.close()
