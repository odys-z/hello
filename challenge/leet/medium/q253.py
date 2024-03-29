'''
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from unittest import TestCase
from typing import List
from heapq import heapify, heappop, heappush
from _heapq import heappushpop

class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Faster than 5.20%
        '''
        intervals.sort()
        dicnt = {} # start, (overlapping count = 1, end)
        si, ei = intervals.pop(0)
        dicnt.update({si: (1, ei)})
        maxcnt = 1
        while len(intervals) > 0:
            si, ei = intervals.pop(0)
            
            for k in dicnt:
                if k <= si:
                    cnt, e0 = dicnt.get(k, (0, None))
                    if si < e0:
                        if k < si:
                            dicnt.update({k: (cnt, si)})
                        if e0 <= ei:
                            dicnt.update({si: (cnt+1, e0)}), 
                            # dicnt.update({e0: (1, ei)}) 
                            intervals.insert(0, [e0, ei])
                            intervals.sort()
                        elif ei < e0:
                            dicnt.update({si: (cnt+1, ei)}), 
                            # dicnt.update({ei: (1, e0)}) 
                            for _ in range(cnt): # maybe used multiple times
                                intervals.insert(0, [ei, e0])
                            intervals.sort()
                        if maxcnt < cnt + 1:
                            maxcnt = cnt + 1;
                        
                        break # interval updated (break into parts)
            else:
                dicnt.update({si: (1, ei)})
        # print(dicnt)
        return maxcnt

class Solution3:
    '''
        Faster than 15%
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # As there is no overlapping, and handled in sorted starting,
        # only the last one is possible been overlapped by an new arranging interval
        arranges = []
        heapify(intervals)

        si, ei = heappop(intervals)
        arranges.append((si, 1, ei))
        maxcnt = 1
        while len(intervals) > 0:
            si, ei = heappop(intervals)
            
            # for s0 in arranges:
            s0, cnt, e0 = arranges[-1]
            if s0 <= si < e0:
                if s0 < si:
                    arranges.append((s0, cnt, si))
                if e0 <= ei:
                    arranges.append((si, cnt+1, e0)), 
                    heappush(intervals, [e0, ei])
                elif ei < e0:
                    arranges.append((si, cnt+1, ei)), 
                    for _ in range(cnt): # maybe used multiple times
                        heappush(intervals, [ei, e0])
                if maxcnt < cnt + 1:
                    maxcnt = cnt + 1;
            else:
                arranges.append((si, 1, ei))
        return maxcnt

class Solution1:
    '''
    faster than 56%
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda intv : intv[0])
        q = []
        heapify(q)
        maxcnt, cnt = 0, 0
        while len(intervals) > 0:
            si, ei = intervals.pop(0)
            nextei = heappushpop(q, ei)
            while nextei <= si:
                cnt -= 1
                nextei = heappop(q)
            heappush(q, nextei)
            cnt += 1
            if maxcnt < cnt:
                maxcnt = cnt
        return maxcnt

class Solution4:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda intv : intv[0])
        q = []
        heapify(q)
        maxcnt, cnt = 0, 0
        while len(intervals) > 0:
            si, ei = intervals.pop(0)
            heappush(q, ei)
            while q[0] <= si:
                cnt -= 1
                heappop(q)
            cnt += 1
            if maxcnt < cnt:
                maxcnt = cnt
        return maxcnt

class Solution:
    '''
        We allocate meeting rooms greedily, but return it reluctantly,
        unless been driven out - always maximum in use.
    '''
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda intv : intv[0])
        lazys = [intervals[0][1]]
        
        for si, ei in intervals[1:]:
            if si >= lazys[0]:
                heappop(lazys)
            heappush(lazys, ei)
        
        return len(lazys)

class SolutionError:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda intv : -intv[1])
        
        s0, e0 = intervals[0]
        s9 = s0 # latest start
        cnt, mxct = 1, 1

        for s, e in intervals[1:]:
            if s0 < e <= e0:
                cnt += 1
                mxct = max(mxct, cnt)
            if s0 < s and s9 < s :
                cnt -= 1
            s9 = max(s0, s)
            e0 = e # e0 is earliest - sorted like this 
        return mxct
            
if __name__ == "__main__":
    t = TestCase()
    s = Solution()
    t.assertEqual(1, s.minMeetingRooms([[13,15],[1,13]]))
    t.assertEqual(2, s.minMeetingRooms([[0,30],[5,10],[15,20]]))
    t.assertEqual(1, s.minMeetingRooms([[7,10],[2,4]]))
    t.assertEqual(3, s.minMeetingRooms([[0,30],[5,10],[15,20],[7,10]]))
    t.assertEqual(3, s.minMeetingRooms([[0,30],[5,10],[15,20],  [7,10],[2,4]]))
    t.assertEqual(4, s.minMeetingRooms([[0,30],[5,10],[15,20],  [7,10],[2,4], [12, 14], [3, 15]]))
    t.assertEqual(2, s.minMeetingRooms([[1,5],[8,9],[8,9]]))
    t.assertEqual(4, s.minMeetingRooms([[2,7],[6,8],[5,10],[1,9],[3,4]]))
    # {65: (2, 165), 19: (1, 65), 797: (1, 807), 165: (3, 221), 424: (3, 507), 314: (2, 351), 507: (2, 797), 221: (1, 314), 351: (3, 424)}
    t.assertEqual(4, s.minMeetingRooms([[65,424],[351,507],[314,807],[19,797],[165,221]]))
    t.assertEqual(6, s.minMeetingRooms([[65,424],[351,507],[314,807],[387,722],[19,797],[259,722],[165,221]]))
    t.assertEqual(7, s.minMeetingRooms([[65,424],[351,507],[314,807],[387,722],[19,797],[259,722],[165,221],[136,897]]))
    
    
    
    print('OK!')