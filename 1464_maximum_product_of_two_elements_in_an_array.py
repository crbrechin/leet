class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()

        n1, n2 = nums[-1], nums[-2]

        return (n1 - 1) * (n2 - 1)
