'''
Created on 15 Jan 2021

@author: Odys Zhou
'''
from unittest import TestCase
from typing import List

def assertStrsEqual(a: List[str], b: List[str]) -> None:
    t = TestCase()
    t.assertEqual(len(a), len(b))
    a_, b_ = [] * len(a), [] * len(b)
    for e in a:
        a_.append(sorted(e))

    for e in b:
        b_.append(sorted(e))
    
    t.assertCountEqual(a_, b_)


def assertIntsEqual(a: List[int], b: List[int]) -> None:
    t = TestCase()
    t.assertEqual(len(a), len(b))
    a, b = sorted(a), sorted(b)
    for x in range(len(a)):
        t.assertCountEqual(a[x], b[x])

if __name__ == '__main__':
    pass