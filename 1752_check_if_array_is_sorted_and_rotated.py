class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i in range(len(nums) - 1):
            n,m = nums[i],nums[i+1]
            if n > m:
                c += 1
        
        # Complete the loop
        if nums[0] < nums[-1]:
            c += 1
        
        return c <= 1
