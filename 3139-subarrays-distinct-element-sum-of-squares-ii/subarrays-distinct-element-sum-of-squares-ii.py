class Solution(object):
    def sumCounts(self, nums):
        mod = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        sq = [0] * (4 * n)

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                sq[node] = (sq[node] + 2 * tree[node] + (r - l + 1)) % mod
                tree[node] = (tree[node] + (r - l + 1)) % mod
                lazy[node] += 1
                return

            mid = (l + r) // 2

            if lazy[node]:
                for child, a, b in [(node * 2, l, mid),
                                    (node * 2 + 1, mid + 1, r)]:
                    sq[child] = (sq[child] + 2 * tree[child] * lazy[node]
                                 + (b - a + 1) * lazy[node] * lazy[node]) % mod
                    tree[child] = (tree[child] + (b - a + 1) * lazy[node]) % mod
                    lazy[child] += lazy[node]
                lazy[node] = 0

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % mod
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % mod

        ans = 0
        last = {}

        for i, x in enumerate(nums):
            p = last.get(x, -1) + 1
            update(1, 0, n - 1, p, i)
            last[x] = i
            ans = (ans + sq[1]) % mod

        return ans