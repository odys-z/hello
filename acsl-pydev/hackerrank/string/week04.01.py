'''
    https://www.hackerrank.com/challenges/find-a-string/problem
'''

def count_substring(s, ss):
    sl = len(s)
    ssl = len(ss)
    c = 0
    for i in range (sl - ssl):
        if s[i:i+ssl] == ss:
            c += 1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
