
'''
<a href='https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/'>
Asterisks in Python: what they are and how to use them</a>

'''

def get_multiple(*keys, dictionary, default=None):
    ''' The arguments dictionary and default come after *keys, which means they can
        only be specified as keyword arguments. If we try to specify them positionally
        we’ll get an error:
        
        TypeError: get_multiple() missing 1 required keyword-only argument: 'dictionary'
    '''
    return [
        dictionary.get(key, default)
        for key in keys
    ]

fruits = {'lemon': 'yellow', 'orange': 'orange', 'tomato': 'red'}

'''
Traceback (most recent call last):
  File "app.py", line 9, in <module>
    s = get_multiple('lemon', 'tomato', 'squash', fruits, default='unknown')
TypeError: get_multiple() missing 1 required keyword-only argument: 'dictionary'

s = get_multiple('lemon', 'tomato', 'squash', fruits, default='unknown')
'''
s = get_multiple('lemon', 'tomato', 'squash', dictionary = fruits, default='unknown')
''' ['yellow', 'red', 'unknown'] '''
print(s)
