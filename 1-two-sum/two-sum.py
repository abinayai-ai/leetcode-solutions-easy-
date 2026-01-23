class Solution:
    def twoSum(self, nums, target):
        seen = {}  # number : index

        for i in range(len(nums)):
            need = target - nums[i]

            if need in seen:
                return [seen[need], i]

            seen[nums[i]] = i