
from bisect import bisect_right

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        nums = nums[::-1]
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        values = []
        counts = []
        pref_count = []
        pref_sum = []

        ans = 0

        for right in range(n):
            x = nums[right]
            cnt = 1

            while values and values[-1] <= x:
                cnt += counts.pop()
                values.pop()
                pref_count.pop()
                pref_sum.pop()

            pc = pref_count[-1] if pref_count else 0
            ps = pref_sum[-1] if pref_sum else 0

            values.append(x)
            counts.append(cnt)
            pref_count.append(pc + cnt)
            pref_sum.append(ps + x * cnt)

            lo, hi = 0, right

            while lo < hi:
                mid = (lo + hi) // 2

                idx = bisect_right(pref_count, mid)
                prev_count = pref_count[idx - 1] if idx > 0 else 0
                prev_sum = pref_sum[idx - 1] if idx > 0 else 0

                max_sum = pref_sum[-1] - prev_sum
                max_sum -= (mid - prev_count) * values[idx]

                cost = max_sum - (prefix[right + 1] - prefix[mid])

                if cost <= k:
                    hi = mid
                else:
                    lo = mid + 1

            ans += right - lo + 1

        return ans
