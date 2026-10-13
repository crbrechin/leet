class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums[:] = [abs(i) for i in nums]
        nums.sort()
        m = len(nums) // 2

        return sum(n2**2 for n2 in nums[m:]) - sum(n1**2 for n1 in nums[:m])
