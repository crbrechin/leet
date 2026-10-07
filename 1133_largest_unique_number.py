class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        x = max(nums)
        hash = [0] * (x + 1)
        
        for n in nums:
            hash[n] += 1
        
        # print(f'{hash}') # DEBUG
        # print(f'{x}') # DEBUG
        # print(f'{hash[x]}') # DEBUG
        while x > -1:
            
            if hash[x] == 1:
                return x
            else:
                # print(f'{x}') # DEBUG
                x -= 1
        return x
