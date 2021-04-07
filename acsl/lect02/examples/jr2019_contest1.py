'''
http://www.datafiles.acsl.org/samples/contest1/C_1_JR_Transform.pdf
'''

class Solution():
    def numTrans(self, num: str) -> str:
        npd = num.split()
        n, p, d = npd[0], int(npd[1]), int(npd[2])
        np = int(n[-p])
        if np <= 4:
            np = (np + d) % 10
        else:
            np = abs(np - d)
            # get the leftmost digit
            while np >= 10:
                np //= 10

        # bug here
        n = n[:-p] + str(np)
        for px in range(-p + 1, 0):
            n += '0'

        return n

p_ = Solution().numTrans('7145032 2 8')
print(p_)
p_ = Solution().numTrans('124987 2 3')
print(p_)
p_ = Solution().numTrans('124987 6 3')
print(p_)
p_ = Solution().numTrans('124987 2 523')
print(p_)
p_ = Solution().numTrans('4386709 1 2')
print(p_)
