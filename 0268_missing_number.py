class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        m = [0] * n
        for i in nums:
            m[i] += 1
        
        return m.index(0)
