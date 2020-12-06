'''
    https://www.hackerrank.com/challenges/python-mutations/problem
'''
def mutate_string(s, p, ch):
    if p < 0 or p >= len(s):
        return s
    return s[:p] + ch + s[p+1:]

'''
    Reverse String
    --------------

    Problem:
        Given a string, reverse the characters order so that the last at first,
        the penultimate at the second, etc.

    Example:
        'ab cd' -> 'dc ba'
'''
def reverese_str(s):
    # ternary operator version:
    # return None if s is None else s[::-1]
    # or:
    if s is None:
        return None
    else:
        return s[::-1]

'''
    Reverse List
    ------------

    Problem:
        Given a list, reverse the elements' order so that the last at first,
        the penultimate at the second, etc.

    Example:
        ['a', 'b'] -> ['b', 'a']
'''
def reverese_lst(s):
    return None if s is None else s[::-1]

'''
    Reverse Words
    -------------

    Problem:
        Given a string with space and words, reverse the words so make the last
        at first, the penultimate at the second, etc. Replacing each space with '.'

    Example:
        'ab cd' -> 'cd.ab'

'''
def reverse_words(s):
    ss = s.split(' ')
    return '.'.join(ss[::-1])
