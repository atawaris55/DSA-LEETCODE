
class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        ans = [1] * n
        last = [-1] * 26

        def dfs(node):
            idx = ord(s[node]) - ord('a')

            old = last[idx]
            last[idx] = node

            for child in tree[node]:
                dfs(child)

            p = old if old != -1 else parent[node]

            if p != -1:
                ans[p] += ans[node]

            last[idx] = old

        dfs(0)

        return ans
