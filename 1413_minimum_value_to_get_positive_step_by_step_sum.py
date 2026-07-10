class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s = 0
        prefix = []
        for n in nums:
            s += n
            prefix.append(s)
        
        # print(f'{prefix}') # DEBUG
      
        # What would be the minimum value required to bring the value of startingValue to 1?
        return 1 - min(prefix) if min(prefix) < 1 else 1
