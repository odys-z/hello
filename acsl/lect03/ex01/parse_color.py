
def parseColor(col: str):   # "col: str" shows the argument is a str type
    if (col[0] == '#' and len(col) == 7):
        r = int(col[1] + col[2], base = 16)
        g = int(col[3] + col[4], base = 16)
        b = int(col[5] + col[6], base = 16)
        return (r, g, b)
    else:
        return (0, 0, 0)
