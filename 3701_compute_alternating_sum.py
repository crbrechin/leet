class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(n * (-1) ** i for i,n in enumerate(nums))
