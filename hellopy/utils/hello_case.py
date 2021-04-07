'''
Test case helper

Created on 24 Dec 2019

@author: ody
'''
from utils.Assrt import XdArrParser

class FileCase(object):
    '''
    '''

    def __init__(self, params = None):
        pass
        
    def loadArr(self, fpath, dimension = 1):
        arrs = list()
        xparser = XdArrParser(dimension)
        with open(fpath, 'r') as f:
            ln = '#'
            while ln:
                if ln[0] in '#\n':
                    ln = f.readline()
                    continue

                arr = xparser.parseInt(ln)
                arrs.append(arr)
                ln = f.readline()
        
        return arrs

