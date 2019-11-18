'''
Test create object with class name
see answer by S.Lott
https://stackoverflow.com/questions/3451779/how-to-dynamically-create-an-instance-of-a-class-in-python

Created on 18 Nov 2019

@author: odys-z@github.com
'''
from importlib import import_module

import tutorial.foo.Foo # @UnusedImport

def creatByName(class_str: str = 'tutorial.foo.Foo.Class1'):
    try:
        module_path, class_name = class_str.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, class_name), eval(class_str)()
    except (ImportError, AttributeError) as e: # @UnusedVariable
        raise ImportError(class_str)

if __name__ == '__main__':
    c, o = creatByName()
    print(c, o, o.type)
