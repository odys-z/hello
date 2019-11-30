'''
Created on 18 Nov 2019

@author: odys-z@github.com
'''

class Class1(object):
    '''
    classdocs
    '''


    def __init__(self, type = 'io.odysz.hello.test.Class1'):
        '''
        Constructor
        '''
        self.type = type
        
class Sub1(Class1):
    pass