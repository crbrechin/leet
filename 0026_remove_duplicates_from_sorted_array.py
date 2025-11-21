class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums)) # Get unique, overwrite
        nums[:] = sorted(nums, key = lambda x: x) # Then sort
        # print(nums) # DEBUG
        return len(nums)
