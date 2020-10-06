import unittest

from add_nums import SolutionLeetCode1, SolutionLeetCode2, SolutionACSL1

class Test(unittest.TestCase):
    def q415(self):
        s = SolutionLeetCode2() 
        self.assertEqual('0', s.addStrings('0', '0'))
        self.assertEqual('1', s.addStrings('1', '0'))
        self.assertEqual('3', s.addStrings('1', '2'))
        self.assertEqual('10', s.addStrings('1', '9'))
        self.assertEqual('11', s.addStrings('1', '10'))
        self.assertEqual('11', s.addStrings('2', '9'))
        self.assertEqual('30', s.addStrings('1', '29'))
        self.assertEqual('100', s.addStrings('1', '99'))
        self.assertEqual('1000', s.addStrings('1', '999'))
        self.assertEqual('1008', s.addStrings('9', '999'))
        self.assertEqual('1998', s.addStrings('999', '999'))
        self.assertEqual('110', s.addStrings('96', '14'))
        self.assertEqual('1010', s.addStrings('906', '104'))
        self.assertEqual('1234567903332', s.addStrings('12345', '1234567890987'))
        self.assertEqual('99099110110', s.addStrings('99099099099', '11011'))
t = Test()
t.q415()
