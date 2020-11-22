from unittest import TestCase

def your_func():
    # here is your program
    return 'Hi!'

t = TestCase()
t.assertEqual('Hi!', your_func())
print('OK!')