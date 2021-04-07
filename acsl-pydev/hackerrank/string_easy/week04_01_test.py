from unittest.case import TestCase

from string_easy.week04_01 import swap_case

t = TestCase()
t.assertEqual('1', swap_case('1'))
t.assertEqual('asddvece', swap_case('ASDDVECE'))
t.assertEqual('asDDvEC31.ACIe', swap_case('ASddVec31.aciE'))
t.assertEqual('121131114111A A1511116', swap_case('121131114111a a1511116'))

print('\nTest OK: swap_case')
