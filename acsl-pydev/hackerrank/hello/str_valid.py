'''
hackerrank problem
------------------

https://www.hackerrank.com/challenges/string-validators/problem

test case:
----------

    #$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh ui s 0hrem89m4c02mw4xo;,wh fwhmxlxfkjsaxu83v 08 n8OHIOM 03J J3L;JMFC3JM3JC3'J N090N9 OOHOLNHNLLKNLKNKNKKKK33300

'''

# WRONG ANSWER
# correct reference: <res>/hackerrank/str_valid.py
if __name__ == '__main__':
    s = input()
    yan = s.isalnum()
    print(yan)
    nn = not s.isdigit()
    print(yan and nn)
    na = not s.isalpha()
    print(yan and na)
    print(yan and nn and not s.isupper())
    print(yan and nn and not s.islower())
