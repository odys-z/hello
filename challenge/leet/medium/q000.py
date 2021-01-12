'''
Created on 12 Jan 2021

@author: Odys Zhou
'''
import unittest


class Test0(unittest.TestCase):
    def __init__(self, name):
        self.name = name
        pass

    def t000(self): 
        print("test {}".format(self.name))


if __name__ == "__main__":
    
    t = Test0("000")
    t.t000()
    
    print('OK!')