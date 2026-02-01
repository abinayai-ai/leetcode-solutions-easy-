class Solution:
    def minimumCost(self, nums):
        n = len(nums)
        
        first_cost = nums[0]
        
        # Smallest value for second subarray start
        min1 = nums[1]
        
        # Best sum of second + third subarray starts
        min_sum = float('inf')
        
        for j in range(2, n):
            # nums[j] is start of third subarray
            min_sum = min(min_sum, min1 + nums[j])
            
            # Update smallest start for second subarray
            min1 = min(min1, nums[j])
        
        return first_cost + min_sum

        