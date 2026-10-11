class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(x ** 2 for i, x in enumerate(nums) if len(nums) % (i + 1) == 0)
