class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x in nums: # Start
            if nums.count(x) == 1: # Compare
                return x # Return
