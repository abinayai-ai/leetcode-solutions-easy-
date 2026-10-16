class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        sums = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, v):
            length = r - l + 1
            tree[node] = (
                tree[node] + 2 * v * sums[node] + v * v * length
            ) % MOD
            sums[node] = (sums[node] + v * length) % MOD
            lazy[node] += v

        def push(node, l, r):
            if lazy[node] and l != r:
                mid = (l + r) // 2
                v = lazy[node]
                apply(node * 2, l, mid, v)
                apply(node * 2 + 1, mid + 1, r, v)
                lazy[node] = 0

        def update(node, l, r, ql, qr, v):
            if ql <= l and r <= qr:
                apply(node, l, r, v)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr, v)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr, v)

            sums[node] = (sums[node * 2] + sums[node * 2 + 1]) % MOD
            tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            p = last.get(x, -1) + 1
            update(1, 0, n - 1, p, i, 1)
            ans = (ans + tree[1]) % MOD
            last[x] = i

        return ans
        