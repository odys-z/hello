from typing import List
from unittest import TestCase

class MinHeap:
	'''
	Implement a min-heap
	'''

	def __init__(self, comparator = None):
		self.judge = comparator
		self.h = []

	def peek(self):
		return self.h[0]

	def count(self):
		return len(self.h)

	def pop(self):
		t = self.h[0]
		self.h[0] = self.h[-1]
		self.h = self.h[:-1]
		# move then compete downward
		p, l, r = 0, 1, 2
		while p < len(self.h):
			# child = index of min(h[l], h[r])
			child = l
			if l < len(self.h) and r < len(self.h) and self.h[l] > self.h[r]:
				child = r
			if child < len(self.h):
				self.h[p], self.h[child] = self.h[child], self.h[p]
			p, l, r = child, child * 2 + 1, child * 2 + 2
		return t

	def push(self, v) -> 'MinHeap':
		self.h.append(v)
		# competing upward
		c = len(self.h) - 1
		p = (c - 1) // 2
		while p >= 0:
			if self.h[p] > self.h[c]:
				self.h[p], self.h[c] = self.h[c], self.h[p]
			p, c = (c - 1) // 2, p
		return self

	def pushList(self, l: List) -> 'MinHeap':
		for v in l:
			self.push(v)

if __name__ == '__main__':
    t = TestCase()
    h = MinHeap()
    h.pushList([1, 0, 2, 3, 4])
    t.assertEqual(0, h.pop())
    t.assertEqual(1, h.peek())
    v = h.push(5).pop()
    t.assertEqual(1, v)
    v = h.push(7).pop()
    t.assertEqual(2, v)
    v = h.push(9).pop()
    t.assertEqual(3, v)
    v = h.push(10).pop()
    t.assertEqual(4, v)
    t.assertEqual(5, h.pop())
    t.assertEqual(7, h.pop())
    t.assertEqual(9, h.peek())
    t.assertEqual(9, h.pop())
    t.assertEqual(10, h.peek())
    t.assertEqual(1, h.count())

    print('OK!')
