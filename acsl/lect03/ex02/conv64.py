radix64 = [
    '0', '1', '2', '3', '4', '5', '6', '7',
    '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z', '+', '-'
]

def conv_64(n: str) -> str:
    v64 = ''
    v10 = int(n)
    if v10 == 0:
        return '0'

    while v10 > 0:
        digit64 = v10 % 64
        v10 //= 64            # a // b return an integer
        v64 = radix64[digit64] + v64

    return v64
