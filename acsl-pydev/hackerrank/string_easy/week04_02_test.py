from unittest.case import TestCase

from string_easy.week04_02 import *

t = TestCase()
t.assertEqual('a', mutate_string('1', 0, 'a'))
t.assertEqual('1a314', mutate_string('11314', 1, 'a'))

t.assertEqual('ab', reverese_str('ba'))
t.assertEqual('ab', reverese_lst('ba'))
t.assertEqual(['a', 'b'], reverese_lst(['b', 'a']))
t.assertEqual(['a', 'b'], reverese_str(['b', 'a']))

print('\nTest OK: mutate_string')
