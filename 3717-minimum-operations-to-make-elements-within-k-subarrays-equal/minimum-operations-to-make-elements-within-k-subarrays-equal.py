from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        low = []
        high = []
        dead = defaultdict(int)

        ls = hs = 0
        lsum = hsum = 0

        def prune(heap, sign):
            while heap:
                v = heap[0] * sign
                if dead[v]:
                    dead[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal ls, hs, lsum, hsum

            prune(low, -1)
            prune(high, 1)

            while ls > hs + 1:
                prune(low, -1)
                v = -heapq.heappop(low)
                ls -= 1
                lsum -= v
                heapq.heappush(high, v)
                hs += 1
                hsum += v

            while ls < hs:
                prune(high, 1)
                v = heapq.heappop(high)
                hs -= 1
                hsum -= v
                heapq.heappush(low, -v)
                ls += 1
                lsum += v

            prune(low, -1)
            prune(high, 1)

        def add(v):
            nonlocal ls, hs, lsum, hsum

            prune(low, -1)

            if not low or v <= -low[0]:
                heapq.heappush(low, -v)
                ls += 1
                lsum += v
            else:
                heapq.heappush(high, v)
                hs += 1
                hsum += v

            balance()

        def remove(v):
            nonlocal ls, hs, lsum, hsum

            prune(low, -1)
            prune(high, 1)

            dead[v] += 1

            if v <= -low[0]:
                ls -= 1
                lsum -= v
            else:
                hs -= 1
                hsum -= v

            balance()

        def get_cost():
            m = -low[0]
            return m * ls - lsum + hsum - m * hs

        costs = []

        for i in range(x):
            add(nums[i])

        costs.append(get_cost())

        for i in range(x, n):
            remove(nums[i - x])
            add(nums[i])
            costs.append(get_cost())

        # DP with rolling arrays
        INF = 10**18
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]