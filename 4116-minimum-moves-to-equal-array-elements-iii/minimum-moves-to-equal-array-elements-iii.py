class Solution(object):
    def minMoves(self, nums):
        moves=0
        v=max(nums)
        for i in range(len(nums)):
            moves+=v-nums[i]
        return moves
        