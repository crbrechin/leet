class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # print(len(nums)) # DEBUG
        return [x for x in range(0,len(nums)+1) if x not in nums][0]
        # print(i) # DEBUG
