'''
    https://www.hackerrank.com/challenges/find-a-string/problem
    
    test cases:
    -----------
    
    ABCDCDC CDC -> 2
    1232356 3   -> 2
    1 33        -> 0
    1211311141111511116 11    -> 9
    
'''
def count_substring(s, ss):
    sl = len(s)
    ssl = len(ss)
    c = 0
    if (ssl > 0 and ssl <= sl):
        for i in range (sl - ssl + 1):
            if s[i:i+ssl] == ss:
                c += 1
    return c

if __name__ == '__main__':
    string = input("string:\t").strip()
    sub_string = input("sub-string: ").strip()

    count = count_substring(string, sub_string)
    print(count)
