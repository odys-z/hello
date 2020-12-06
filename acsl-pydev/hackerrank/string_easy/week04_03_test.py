from unittest.case import TestCase

from string_easy.week04_03 import count_substring

t = TestCase()
t.assertEqual(1, count_substring('1', '1'))
t.assertEqual(2, count_substring('ASDDVECE', 'E'))
t.assertEqual(2, count_substring('ASDDVECE', 'D'))
t.assertEqual(9, count_substring('1211311141111511116', '11'))

print('\nTest OK: count_substring')
