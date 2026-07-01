class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        left,right = 0,0
        consecutive = 0

        while right < len(nums):
            # print(f'{nums[left:right]}') # DEBUG
            if nums[right] == 0:
                left = right + 1
                right = left
            else:
                right += 1
                consecutive = max(consecutive, len(nums[left:right]))
        
        return consecutive
             
