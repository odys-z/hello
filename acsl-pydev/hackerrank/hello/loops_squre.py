'''
    https://www.hackerrank.com/challenges/python-loops/problem
    
    Task
    ====

    The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

    Example
    =======

    The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

    0
    1
    4

    Input Format
    ============

    The first and only line contains the integer, .

    Constraints
    ===========


    Output Format
    ===========

    Print  lines, one corresponding to each .

    Sample Input 0

    5

    Sample Output 0

    0
    1
    4
    9
    16
'''
if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    print(a[0])
    
    for i in range(1, n):
        a[i] = a[i-1] + ((i-1) << 1) + 1 
        # i         , 1, 2, 3
        # 2(i-1)+1 0, 1, 3, 5
        # a[i]     0, 1, 4, 9
        print(a[i])



