'''
    s = 2, delta = 3, rows = 5
    
    2
    5    10
    13   16    21
    24   27    32    35
    40   43    46    51    54
    
    s = 221, d = 2, r = 4
    
    221
    223   225
    227   231   233
    235   237   241   243


    0    s                                    s        + 0  (r = 1)
    1    s + d,  s + 2d                       s + d    + 1  (r = 2)
    2    s + 3d, s + 4d, s + 5d               s + 3d   + 2  (r = 3)
    3    s + 6d, s + 7d, s + 8d, s + 9d       s + 6d   + 3  (r = 4)

    r    s0,     s0 + d, s0 + 2d, ...         s + (r(r-1)/2) d
'''

mathArr = '''
Triangle Printout
=================

.. math::
    
    s = {s:}, d = {d:}, r = {r:}

    \\begin\{array\}\{{colsAlign:}\}
{rows}
    \\hline
    \\end\{array\}
..
'''

mathRow = '{row} \\\\'

def row(cells: list) -> str:
    r = ''
    for c in cells:
        if r != '':
            r += ' & '
        r += str(c)
    return r
        
def rmDigits(n):
    '''
        the number minus digits
    '''

s = 2, d = 3, r = 5
f = open("inter.rst", "w")
f.write(mathArr.format(s, d, r, colsAlign, rows)
f.close()
