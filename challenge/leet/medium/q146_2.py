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

class Bilinst():
    def __init__(self):
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.lru.prev, self.mru.nxt = self.mru, self.lru
    
    def enque(self, node):
        mr = self.mru
        mr.nxt.prev, node.nxt = node, mr.nxt
        mr.nxt, node.prev = node, mr 
    
    def remove(self, node):
        node.nxt.prev, node.prev.nxt = node.prev, node.nxt
        
    def getLRU(self):
        return self.lru.prev.k

class LRUCache:

    def __init__(self, capacity: int):
        self.bilinst = Bilinst()
        self.kv = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        n = self.kv.get(key, None)
        if n is None:
            return -1

        self.bilinst.remove(n)
        self.bilinst.enque(n)
        return n.v

    def put(self, key: int, value: int) -> None:
        n = self.kv.get(key)
        if n is None:
            if len(self.kv) == self.capacity:
                # remove
                lru = self.kv.pop(self.bilinst.getLRU())
                self.bilinst.remove(lru)
            n = Node(key, value)
        else:
            self.bilinst.remove(n)
            n.v = value

        self.kv[key] = n
        self.bilinst.enque(n)


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

    print('OK!')
