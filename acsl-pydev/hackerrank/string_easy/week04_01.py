'''
    https://www.hackerrank.com/challenges/swap-case/problem
'''
def swap_case(s):
    s1 = ''
    for i in range(len(s)):
        if s[i].isupper():
            s1 += s[i].lower()
        else:
            s1 += s[i].upper()

    return s1
