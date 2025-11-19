class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val] # Use [:] so that it is "in-place"
        return len(nums)
