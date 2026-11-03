class Solution(object):
    def minMoves(self, nums):
        moves=0
        v=max(nums)
        for i in range(len(nums)):
            if nums[i]!=v:
                moves+=v-nums[i]
        return moves
        