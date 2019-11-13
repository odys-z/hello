
def odds(n):
    odds = [2 * n + 1 for n in range(n ** 2)]
    n2 = 0
    for odd in odds
        n2 += odd
        yield n2
        
def peerMat(n, mat, u, d, l, r):
    for cx in range(l, r - 1)
        print('up row', (u, cx))
        # mat[u][cx] = next(odds)
        mat[u * n + cx] = next(odds)
        
    for rx in range(u, d)
        print('right col', (u, cx))
        # mat[rx][r] = next(odds)
        mat[rx * n + r] = next(odds)

    for cx in range(r - 1, l)
        print('dow row', (d, cx))
        # mat[d][cx] = next(odds)
        mat[d * n + cx] = next(odds)
        
    for rx in range(d - 1, u)
        print('left col', (u, cx))
        # mat[rx][l] = next(odds)
        mat[rx * n + l] = next(odds)
    
    if l + 1 < r:
        peerMat(n, mat, u + 1, d - 1, l + 1, r -1)
       

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
                
        # mat = [[0 for _ in range(n)] for _ in range(n)]
        mat = [0 for _ in range(n ** 2)]
        
        l = 0, r = n - 1 # left right
        u = 0, d = n - 1 # up down
        peerMat(n, mat, u, d, l, r)
        
