'''
 * 661. Image Smoother
 * https://leetcode.com/problems/image-smoother/description/
'''
import unittest
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        buf = [[0] * n for _ in range(m)]

        if n > 1:
            for rx, r in enumerate(img):
                buf[rx][0] = r[0] + r[1]
                if n > 2:
                    for cx in range(1, n - 1):
                        buf[rx][cx] = r[cx - 1] + r[cx] + r[cx + 1]
                buf[rx][-1] = r[-2] + r[-1]
        else:
            img, buf = buf, img

        d0 = 1 if max(m, n) == 1 else 2 if min(m, n) == 1 else 4
        dx = 6 if min(m, n) > 1 else 3
        di = 9
        if m > 1:
            for cx in range(n):
                img[0][cx] = (buf[0][cx] + buf[1][cx]) // (dx if 0 < cx < n - 1 else d0)
                # if m > 2:
                for rx in range(1, m - 1):
                    img[rx][cx] = (buf[rx - 1][cx] + buf[rx][cx] + buf[rx + 1][cx]) // (di if 0 < cx < n - 1 else dx)
                else:
                    img[-1][cx] = (buf[-2][cx] + buf[-1][cx]) // (dx if 0 < cx < n - 1 else d0)
        else:  # m == 1
            for cx in range(n):
                img[0][cx] = buf[0][cx] // (dx if 0 < cx < n - 1 else d0)

        return img


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = Solution()

        self.assertEqual([[3,3]], s.imageSmoother([[1,5]]))
        self.assertEqual([[137, 93, 78, 55], [141, 97, 87, 55], [137, 93, 93, 78]],
             s.imageSmoother([[100, 200, 10, 10], [200, 50, 2, 200], [100, 200, 11, 100]]))
        self.assertEqual([[137, 141, 137], [141, 138, 141], [150, 144, 147], [162, 142, 158]],
             s.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100], [120, 230, 103]]))
        self.assertEqual([[1, 1, 1]], s.imageSmoother([[1, 1, 1]]))
        self.assertEqual([[0, 0, 0], [0, 0, 0], [0, 0, 0]], s.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
        self.assertEqual([[137, 141, 137], [141, 138, 141], [137, 141, 137]],
             s.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
        self.assertEqual([[1], [1]], s.imageSmoother([[1], [1]]))


if __name__ == '__main__':
    unittest.main()
