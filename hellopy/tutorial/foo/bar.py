'''
Created on 18 Nov 2019

@author: odys-z@github.com
'''
from tutorial.foo.foo import Class1

class Bar1(Class1):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Class1.__init__(self, 'io.odysz.test.Bar1')
        