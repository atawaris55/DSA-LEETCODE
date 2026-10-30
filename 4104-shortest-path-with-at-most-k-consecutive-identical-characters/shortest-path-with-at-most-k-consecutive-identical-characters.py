
import heapq

class Solution(object):
    def shortestPath(self, n, edges, labels, k):

        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        dist[0][1] = 0

        pq = [(0, 0, 1)]

        while pq:

            d, u, count = heapq.heappop(pq)

            if d > dist[u][count]:
                continue

            if u == n - 1:
                return d

            for v, w in adj[u]:

                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_dist = d + w

                if new_dist < dist[v][new_count]:
                    dist[v][new_count] = new_dist

                    heapq.heappush(
                        pq, (new_dist, v, new_count)
                    )

        return -1
