
class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix = [0] * n
        timer = 0

        # Build tree using iterative DFS
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                mask = 1 << (ord(s[u]) - ord('a'))
                prefix[u] = mask ^ (prefix[p] if p != -1 else 0)

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        # Binary lifting
        LOG = n.bit_length()
        up = [[0] * n for _ in range(LOG)]

        for u in range(n):
            up[0][u] = parent[u] if parent[u] != -1 else u

        for j in range(1, LOG):
            for u in range(n):
                up[j][u] = up[j - 1][up[j - 1][u]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return up[0][u]

        # Fenwick tree for range XOR updates and point queries
        bit = [0] * (n + 2)

        def update(i, val):
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def range_update(l, r, val):
            update(l, val)
            if r + 1 < n:
                update(r + 1, val)

        def point_query(i):
            i += 1
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        # Apply initial prefix masks
        for u in range(n):
            range_update(tin[u], tin[u], prefix[u])

        chars = list(s)
        ans = []

        for q in queries:
            parts = q.split()
            typ = parts[0]
            u = int(parts[1])

            if typ == "update":
                c = parts[2]

                old_mask = 1 << (ord(chars[u]) - ord('a'))
                new_mask = 1 << (ord(c) - ord('a'))
                diff = old_mask ^ new_mask

                if diff:
                    range_update(tin[u], tout[u], diff)
                    chars[u] = c

            else:
                v = int(parts[2])

                pu = point_query(tin[u])
                pv = point_query(tin[v])
                w = lca(u, v)

                path_mask = pu ^ pv ^ (
                    1 << (ord(chars[w]) - ord('a'))
                )

                ans.append((path_mask & (path_mask - 1)) == 0)

        return ans
