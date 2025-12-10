class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target) # If it's there
        else: # Otherwise
            c = 0 # Start at the first
            for i in nums:
                if i < target: # If less than
                    c += 1 # Move to next
            return c
