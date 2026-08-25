class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        dic = set(nums)
        # print(f'{dic}') # DEBUG
        
        for i in range(1, len(nums) + 1):
            if k * i not in dic:
                return k * i
        
        return k * (len(nums) + 1)
