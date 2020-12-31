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

from print_triangle import printOctalRows

mathArr = '''
Triangle Printout
=================

.. math::

    s = {s:}, d = {d:}, r = {r:}

    \\begin{{array}}{{{colsAlign:}}}
    \\hline
{rows}
    \\hline
    \\end{{array}}
..
'''

mathRow = '{row} \\\\'

def row(cells: list) -> str:
    r = ''
    for c in cells:
        if r != '':
            r += ' & '
        r += str(c)
    r += ' \\\\'
    return r

def rmDigits(s, d, r):
    '''
        the numeral triangles

    .. math::

        \begin{array}{cl}
        f(n) & = n ⋅ f(n - 1) \\
        \hline
        5! & = 5 ⋅ f(4)_? \\
        \end{array}
    ..
    '''
    return '    1 & 2 \\'


if __name__ == '__main__':
    s, d, r = 2, 3, 5
    f = open("inter_.rst", "w")
    colsAlign = 'c' * (r + 1)
    # rows = rmDigits(s, d, r)
    rows = printOctalRows('{:3d} ({:2d}, {:2d})', s, d, r)
    f.write(mathArr.format(s=s, d=d, r=d, colsAlign=colsAlign, rows=rows))
    f.close()

    print('OK!')