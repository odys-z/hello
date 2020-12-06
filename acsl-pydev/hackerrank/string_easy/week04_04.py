'''
    https://www.hackerrank.com/challenges/capitalize/problem
    
    test cases:
    -----------
    
        input:
            'q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'

        exprected:
            'Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'
'''

def solve(s):
    if s is not None:
        return ' '.join(map(lambda t: '' if t is None else t.capitalize(), s.split(' ')))
    return ''

