from heapq import *

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        n = len(profits)
        m = [(capital[i], profits[i]) for i in range(n)]
        m.sort()
        pq = []
        i = 0
        for _ in range(k):
            while i < n and m[i][0] <= w:
                heapq.heappush(pq, -m[i][1])
                i += 1
            if not pq:
                break
            w -= heapq.heappop(pq)
        return w