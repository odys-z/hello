'''
https://www.hackerrank.com/challenges/2d-array/problem?h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(a, r0, c0):
    s = 0
    for c in range(c0, c0 + 3):
        s += a[r0][c] + a[r0+2][c]
    s += a[r0+1][c0+1]
    # print(s)
    return s

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxs = float('-inf')

    for y in range(4):
        for x in range(4):
            s = hourglass(arr, y, x)
            if s > maxs:
                maxs = s
    return maxs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
