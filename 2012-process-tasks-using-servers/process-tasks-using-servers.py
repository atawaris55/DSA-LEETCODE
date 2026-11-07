import heapq
from collections import deque

class Solution:
    def assignTasks(self, servers, tasks):
        n, m = len(servers), len(tasks)
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []
        queue = deque()
        res = [0] * m

        for t in range(m):
            while busy and busy[0][0] <= t:
                _, w, idx = heapq.heappop(busy)
                heapq.heappush(free, (w, idx))

            queue.append((t, tasks[t]))

            while queue and free:
                j, dur = queue.popleft()
                w, idx = heapq.heappop(free)
                res[j] = idx
                heapq.heappush(busy, (t + dur, w, idx))

        t = m
        while queue:
            if not free:
                t = max(t, busy[0][0])
                while busy and busy[0][0] <= t:
                    _, w, idx = heapq.heappop(busy)
                    heapq.heappush(free, (w, idx))

            j, dur = queue.popleft()
            w, idx = heapq.heappop(free)
            res[j] = idx
            heapq.heappush(busy, (t + dur, w, idx))

        return res