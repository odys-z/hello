'''
Created on Jan 18, 2021

@author: ody
'''
from unittest import TestCase
from _heapq import heapify, heappush

class Node:
    def __init__(self, v, nxt = None):
        self.v = v
        self.prv = None
        self.nxt = nxt
        
class MinStackReheapify:
    '''
    26%
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = Node(-float('inf'))  # or + ?
        self.hp = [] # (v, idx)
        heapify(self.hp)
        
        
    def push(self, x: int) -> None:
        heappush(self.hp, x)
        n = Node(x, self.head.nxt)
        self.head.nxt = n
        

    def pop(self) -> None:
        q = self.head.nxt
        self.head.nxt = self.head.nxt.nxt
        self.hp.remove(q.v)
        heapify(self.hp)
        return q.v
        

    def top(self) -> int:
        return self.head.nxt.v
        

    def getMin(self) -> int:
        return self.hp[0]
        
class MinStack:
    '''
     96.09%
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.least = float('inf')
        self.stack = []
        
        
    def push(self, x: int) -> None:
        if self.least > x:
            self.least = x
        self.stack.append((x, self.least))
        print(self.stack)
        

    def pop(self) -> None:
        q = self.stack.pop()
        if len(self.stack) == 0:
            self.least = float('inf')
        else: self.least = self.stack[-1][1]
        return q[0]
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    t = TestCase()
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    t.assertEqual(-3, obj.getMin())
    obj.pop()
    t.assertEqual(0, obj.top())
    t.assertEqual(-2, obj.getMin())
    
    '''
    What's wrong:
    input:
    ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    [[],        [2147483646],[2147483646],[2147483647],[],[],[],[],[],[],      [2147483647],[],[],   [-2147483648],[],[],   [],  []]
    
    output/expected:
    [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
    [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]
    '''
    
    '''
    ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
    [[],        [1],   [1],   [2],   [],   [],   [],      [],   [],      [],   [2],   [],   [],      [-3],  [],   [],      [],   []]
    [null,      null,  null,  null,  2,    null, 1,       null, 1,       null, null,  2,    2,       null,  -3,   -3,      null, 2]
    '''
    s = MinStack()
    s.push(1)
    s.push(1)
    s.push(2)
    t.assertEqual(2, s.top())
    s.pop()
    t.assertEqual(1, s.getMin())
    s.pop()
    t.assertEqual(1, s.getMin())
    s.pop()
    s.push(2)
    t.assertEqual(2, s.top())
    t.assertEqual(2, s.getMin())
    s.push(-3)
    t.assertEqual(-3, s.top())
    t.assertEqual(-3, s.getMin())
    s.pop()
    t.assertEqual(2, s.getMin())

    '''
    ["MinStack","push","push","push","top","pop","push","push","getMin"]
    [[],        [-10], [14],  [-20], [],   [],   [10],  [-7],  []]

    [null,      null,  null,  null,  -20,  null, null,  null,  -10]
    '''
    s = MinStack()
    s.push(-10)
    s.push(14)
    s.push(-20)
    t.assertEqual(-20, s.top())
    s.pop()
    s.push(10)
    s.push(-7)
    t.assertEqual(-10, s.getMin())
    print('OK!')

    