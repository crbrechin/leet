class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)

        return sum(abs(m - n) for n in nums)
