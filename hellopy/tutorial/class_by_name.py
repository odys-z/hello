'''
Test create object with class name
see answer by S.Lott
https://stackoverflow.com/questions/3451779/how-to-dynamically-create-an-instance-of-a-class-in-python

Created on 18 Nov 2019

@author: odys-z@github.com
'''
from importlib import import_module

import tutorial.foo.foo # @UnusedImport
from tutorial.foo.foo import Class1

def creatByName(class_str: str = 'tutorial.foo.foo.Class1'):
    try:
        module_path, class_name = class_str.rsplit('.', 1)
        module = import_module(module_path)
        return getattr(module, class_name), eval(class_str)()
    except (ImportError, AttributeError) as e: # @UnusedVariable
        raise ImportError(class_str)

def allSubcls(cls):
    allSubs = []

    for sub in cls.__subclasses__():
        allSubs.append(sub.__name__)
        allSubs.extend(allSubcls(sub))

    return allSubs

if __name__ == '__main__':
    c, o = creatByName()
    # Class1 <tutorial.foo.foo.Class1 object at 0x7f079a9c8f98> 
    # type: io.odysz.hello.test.Class1     subclasses of Class1: ['Sub1']
    print(c.__name__, o, '\ntype: {}'.format(o.type),
          '\tsubclasses of Class1: {}'.format(allSubcls(Class1)))

    c, o = creatByName('tutorial.foo.bar.Bar1')
    # This test case shows that a user defined module.class will be loaded by createByName()
    # Bar1 <tutorial.foo.bar.Bar1 object at 0x7f079a9c8e80> 
    # type: io.odysz.test.Bar1     subclasses of Class1: ['Sub1', 'Bar1']
    print(c.__name__, o, '\ntype: {}'.format(o.type),
          '\tsubclasses of Class1: {}'.format(allSubcls(Class1)))
