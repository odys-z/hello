'''
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

@author: Odys Zhou
'''
import unittest

class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.nxt = None
        self.prev = None

    def follow(self, node):
        if node.nxt and node.nxt.prev:
            node.nxt.prev = self
        self.prev = node

        node.nxt = self

    def remove(self):
        following = self.prev
        if self.nxt:
            self.nxt.prev = self.prev

        if self.prev:
            self.prev.nxt = self.nxt

        return following


class LRUCache:

    def __init__(self, capacity: int):
        self.lru = None
        self.mru = None
        self.kv = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        n = self.kv.get(key, None)
        if n is None:
            return -1

        if self.lru.k == n.k:
            self.lru = n.remove()
        elif self.mru.k == n.k:
            return n.v # self.mru = n.nxt
        else: n.remove()

        self.mru.follow(n)
        self.mru = n
        # self.kv[self.mru.k] = n
        if self.lru is None:
            self.lru = n
        return n.v


    def put(self, key: int, value: int) -> None:
        n = self.kv.get(key)
        if n is None:
            if len(self.kv) == self.capacity:
                # remove
                self.kv.pop(self.lru.k, None)
                self.lru = self.lru.remove()
            n = Node(key, value)
        else:
            n.v = value
            if self.lru.k == n.k:
                self.lru = n.remove()
            else: n.remove()

        if self.mru is not None:
            self.mru.follow(n)
        self.mru = n
        self.kv[key] = n

        if self.lru is None:
            self.lru = n


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':

    t = unittest.TestCase()

    '''
        ["LRUCache", "put",  "put",  "get", "put",  "get", "put",  "get", "get", "get"]
        [[2],        [1, 1], [2, 2], [1],   [3, 3], [2],   [4, 4], [1],   [3],   [4]]

        [null, null, null,           1,    null,    -1,    null,   -1,    3,     4]
    '''
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    t.assertEqual(1, c.get(1))
    c.put(3, 3)
    t.assertEqual(-1, c.get(2))
    c.put(4, 4)
    t.assertEqual(-1, c.get(1))
    t.assertEqual(3, c.get(3))
    t.assertEqual(4, c.get(4))

    '''
    ["LRUCache","put","get","put","get","get"]
    [[1],       [2,1],[2],  [3,2],[2], [3]]
    '''
    c = LRUCache(1)
    c.put(2, 1)
    t.assertEqual(1, c.get(2))
    c.put(3, 2)
    t.assertEqual(-1, c.get(2))
    t.assertEqual(2, c.get(3))

    '''
    ["LRUCache","get","put","get","put","put","get","get"]
    [[2],      [2],   [2,6],[1],  [1,5],[1,2],[1],  [2]]
    [null,     -1,    null, -1,   null, null, 2,    6]
    '''
    c = LRUCache(2)
    t.assertEqual(-1, c.get(2))
    c.put(2, 6)
    t.assertEqual(-1, c.get(1))
    c.put(1, 5)
    c.put(1, 2)
    t.assertEqual(2, c.get(1))
    t.assertEqual(6, c.get(2))

    '''
    ["LRUCache","put","put","get","get","put","get","get","get"]
    [[2],       [2,1],[3,2],[3],  [2],  [4,3],[2],  [3],  [4]]
    [null,      null, null, 2,    1,    null, 1,    -1,   3]
    '''
    c = LRUCache(2)
    c.put(2, 1)
    c.put(3, 2)
    t.assertEqual(2, c.get(3))
    t.assertEqual(1, c.get(2))
    c.put(4, 3)
    t.assertEqual(1, c.get(2))
    t.assertEqual(-1, c.get(3))
    t.assertEqual(3, c.get(4))

    '''
    ["LRUCache","put","put", "put","put", "put", "put", "put","put", "put", "put","get"]
    [[5],       [9,3],[6,14],[3,1],[2,14],[3,27],[2,12],[2,9],[13,4],[8,18],[1,7],[6]]
    [null,      null, null,  null, null,  null,  null,  null, null,  null,  null, -1]
     '''
    c = LRUCache(5)
    c.put(9, 3)
    c.put(6, 14)
    c.put(3, 1)
    c.put(2, 14)
    c.put(3, 27)
    c.put(2, 12)
    c.put(2, 9)
    c.put(13, 4)
    c.put(8, 18)
    c.put(1, 7)
    t.assertEqual(-1, c.get(6))

	'''
	Wrong
	Your input
["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get"]
[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6]]
Output
[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,14]
Expected
[null,null,null,null,null,null,-1,null,19,17,null,-1,null,null,null,-1,null,-1,5,-1,12,null,null,3,5,5,null,null,1,null,-1,null,30,5,30,null,null,null,-1,null,-1,24,null,null,18,null,null,null,null,-1]
	'''
    print('TODO!')
