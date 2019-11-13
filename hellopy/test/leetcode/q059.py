
def odds(n):
    odds = [2 * n + 1 for n in range(n ** 2)]
    n2 = 0
    for odd in odds:
        n2 += odd
        yield n2
        
def peerMat(n, mat, sqrs, u, d, l, r):
    for cx in range(l, r - 1):
        print('up row', (u, cx))
        # mat[u][cx] = next(sqrs)
        mat[u * n + cx] = next(sqrs)
        
    for rx in range(u, d):
        print('right col', (u, cx))
        # mat[rx][r] = next(sqrs)
        mat[rx * n + r] = next(sqrs)

    for cx in range(r - 1, l):
        print('dow row', (d, cx))
        # mat[d][cx] = next(sqrs)
        mat[d * n + cx] = next(sqrs)
        
    for rx in range(d - 1, u):
        print('left col', (u, cx))
        # mat[rx][l] = next(sqrs)
        mat[rx * n + l] = next(sqrs)
    
    if l + 1 < r:
        peerMat(n, mat, sqrs, u + 1, d - 1, l + 1, r -1)
       

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
                
        # mat = [[0 for _ in range(n)] for _ in range(n)]
        mat = [0 for _ in range(n ** 2)]
        
        l = u = 0  # left up
        r = d = n - 1 # right down
        peerMat(n, mat, odds(n), u, d, l, r)
        
        print(mat)
        return [mat[i : i + n] for i in range(0, len(mat),  n)]


s = Solution()
m = s.generateMatrix(3)
print(m)
