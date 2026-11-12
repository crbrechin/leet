class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        streak = 1
        
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                # print(f"Increasing: {nums[i-1]} < {nums[i]}") # DEBUG
                increasing += 1
                decreasing = 1
            elif nums[i-1] > nums[i]:
                # print(f"Decreasing: {nums[i-1]} > {nums[i]}") # DEBUG
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1
                # print(f"Equal: {nums[i-1]} == {nums[i]}") # DEBUG
            streak = max(increasing, decreasing, streak)
        return streak
