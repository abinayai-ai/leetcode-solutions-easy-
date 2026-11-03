class Solution(object):
    def minMoves(self, nums):
        maximum = max(nums)
        moves = 0

        for num in nums:
            moves += maximum - num

        return moves