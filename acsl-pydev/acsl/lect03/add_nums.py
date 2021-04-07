'''
Created on 6 Oct 2020

@author: Odys Zhou

Q 415 Adding Strings
https://leetcode.com/problems/add-strings/

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.

You must not use any built-in BigInteger library or convert the inputs to integer directly.
So this is wrong answer:
    def addStrings(self, num1: str, num2: str) -> str:
        num1=int(num1)
        num2=int(num2)
        return(str(num1 +num2))

Runtime: 36 ms, faster than 86.69%
Memory Usage: 14.6 MB, less than 5.07%
'''
class SolutionLeetCode1:
    def addStrings(self, num1: str, num2: str) -> str:
        ix1 = len(num1) - 1
        ix2 = len(num2) - 1

        sum2 = ['0'] * max(ix1 + 2, ix2 + 2)
        ix = len(sum2) - 1
        carry = 0

        while ix1 >= 0 and ix2 >= 0:
            s = int(num1[ix1]) + int(num2[ix2]) + carry
            v = s % 10
            carry = s // 10
            sum2[ix] = str(v)
            ix, ix1, ix2 = ix - 1, ix1 - 1, ix2 - 1

        # e.g. num1 = 1, num2 = 29,
        # now carry = 1, ix1 point to num2's '2'
        if ix2 >= 0:
            ix1 = ix2
            num1 = num2

        while ix > 0:
            s = int(num1[ix1]) + carry
            v = s % 10
            carry = s // 10
            sum2[ix] = str(v)
            ix, ix1 = ix - 1, ix1 - 1

        print(carry, sum2)
        if carry > 0:
            sum2[0] = '1'
            return ''.join(sum2)
        else:
            return ''.join(sum2[1:])

class SolutionLeetCode2:
    def addStrings(self, num1: str, num2: str) -> str:
        ix1 = len(num1) - 1
        ix2 = len(num2) - 1

        sum2 = ['0'] * max(ix1 + 1, ix2 + 1)
        ix = len(sum2) - 1
        carry = 0

        while ix1 >= 0 and ix2 >= 0: 
            s = int(num1[ix1]) + int(num2[ix2]) + carry
            v = s % 10
            carry = s // 10
            sum2[ix] = str(v)
            ix, ix1, ix2 = ix - 1, ix1 - 1, ix2 - 1

        # e.g. num1 = 1, num2 = 29,
        # now carry = 1, ix1 point to num2's '2'
        if ix2 >= 0:
            ix1 = ix2
            num1 = num2

        while ix1 >= 0 and carry > 0:
            s = int(num1[ix1]) + carry
            v = s % 10
            carry = s // 10
            sum2[ix] = str(v)
            ix, ix1 = ix - 1, ix1 - 1

        if ix1 >= 0: s1 = num1[: ix1 + 1]
        else: s1 = ''

        print(carry, sum2, ix, s1)
        if carry > 0:
            return '1' + s1 + ''.join(sum2)
        elif ix < 0:
            return ''.join(sum2)
        else:
            return s1 + ''.join(sum2[1:])
            

class SolutionACSL1:
    def addStrings(self, num1: str, num2: str) -> str:
        ix1 = len(num1) - 1
        ix2 = len(num2) - 1

        sum2 = ['0'] * max(ix1 + 2, ix2 + 2)
        ix = len(sum2) - 1
        carry = 0

        while ix1 >= 0 and ix2 >= 0:
            '''
            s = int(num1[ix1]) + int(num2[ix2]) + carry
            v = s % 10
            carry = s // 10
            sum2[ix] = str(v)
            '''
            carry, sum2[ix] = sum3(carry, num1, ix1, num2, ix2)
            ix, ix1, ix2 = ix - 1, ix1 - 1, ix2 - 1

        # e.g. num1 = 1, num2 = 29,
        # now carry = 1, ix1 point to num2's '2'
        if ix2 >= 0:
            ix1 = ix2
            num1 = num2

        while ix > 0:
            '''
            s = int(num1[ix1]) + carry
            v = s % 10
            carry = s // 10
            sum2[ix] = str(v)
            '''
            carry, sum2[ix] = sum3(carry, num1, ix1, '0', 0)
            ix, ix1 = ix - 1, ix1 - 1

        print(carry, sum2)
        if carry > 0:
            sum2[0] = '1'
            return ''.join(sum2)
        else:
            return ''.join(sum2[1:])

def sum3(carry, n1, ix1, n2, ix2):
    s = int(n1[ix1]) + int(n2[ix2]) + carry
    return s // 10, str(s % 10)
