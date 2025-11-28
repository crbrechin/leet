class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return [i for i in range(min(nums), max(nums)) if i not in nums]
