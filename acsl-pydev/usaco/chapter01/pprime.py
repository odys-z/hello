'''
ID: odys.zh1
LANG: PYTHON3
TASK: pprime
'''

from typing import List

# len1k, prime1k = 10, [ 2,   3,   5,   7 ]
# https://www.factmonster.com/math-science/mathematics/prime-numbers-facts-examples-table-of-all-up-to-1000
len1k, prime1k = 1000, [
       2,   3,   5,   7,  11,  13,  17,  19,  23,
29,   31,  37,  41,  43,  47,  53,  59,  61,  67,
71,   73,  79,  83,  89,  97, 101, 103, 107, 109,
113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
463, 467, 479, 487, 491, 499, 503, 509, 521, 523,
541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
659, 661, 673, 677, 683, 691, 701, 709, 719, 727,
733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
941, 947, 953, 967, 971, 977, 983, 991, 997]

class Ari:
    def __init__(self, a, b):
        # b <= 100 * 1000 * 1000, size <= b ^ 1/2 // 2 = 5000
        s = int(b ** 0.5 + 1) // 2

        # index = n // 2, ignoring even number
        self.primes = [0 for _x in range(s)]
        for p in prime1k:
            if p // 2 >= s: break
            self.primes[p//2] = p
        self.primes[0] = 2
        '''
        for i in range(len1k // 2, s):
            i_2 = i ** 0.5
            for dividor in self.primes:
                if dividor > i_2:
                    break
                if dividor > 0 and i % dividor == 0:
                    self.primes[i//2] = 0
                    break
        '''
        # len1k is even
        for digit in range(len1k + 1, s * 2, 2):
            if self.isPrime(digit):
                self.primes[digit//2] = digit
            
        # end: we have all primes less than b now

    def isPrime(self, v):
        sqrv = v ** 0.5
        for d in self.primes:
            if d > sqrv:
                return True
            elif d > 0 and v % d == 0:
                return False
        else:
            return True

    def prog(self, a, b):
        maxlen = len(str(b))
        
        def sumdigits(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        
        def parlindrom(ans, midigits, midsum, midlen) -> None:
            if midlen >= maxlen: return
            for digit in range(10):
                v = digit * 10 ** (midlen + 1) + midigits * 10 + digit
                if v > b: break

                if digit == 5 or digit == 0 or digit % 2 == 0 or (midsum + digit + digit) % 3 == 0:
                    pass
                elif v % 2 == 0:
                    continue
                elif a <= v <= b and self.isPrime(v):
                    ans.append(v)
                
                parlindrom(ans, v, midsum+2*digit, midlen+2)
        
        ans = []
        for mid in range(10):
            if a <= mid <= b and mid in [2, 3, 5, 7]:
                ans.append(mid)
            parlindrom(ans, mid, sumdigits(mid), 1)
        parlindrom(ans, 0, 0, 0)
        return sorted(ans)

if __name__ != '__main__':
    from unittest import TestCase

    print(__name__)
    t = TestCase() 
    a = Ari(5, 500) 

    ans = a.prog(5, 500)
    print(ans)
    t.assertCountEqual([5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383],
                       ans)
    print('OK!')

else:
    def outputLines(intArr2: List[int]) -> int:
        f = open('pprime.out', 'w')
        for s in intArr2:
            f.write('{}\n'.format(s))
        f.close()
        return len(intArr2)
 
    fin = open('pprime.in', 'r')
    l = fin.readlines()
    fin.close()
    l = l[0].split()
    a, b = int(l[0]), int(l[1])

    g = Ari(a, b)
    ans = g.prog(a, b) 
    outputLines(ans)
