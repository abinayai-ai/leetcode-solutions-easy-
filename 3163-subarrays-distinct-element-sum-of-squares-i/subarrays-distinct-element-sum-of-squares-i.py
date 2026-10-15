
class Solution(object):
    def sumCounts(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            s = set()

            for j in range(i, n):
                s.add(nums[j])
                ans += len(s) * len(s)

        return ans






