class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        mn = float('inf')

        for n in nums:
            s = 0
            while n:
                s += n % 10
                n //= 10
            mn = min(mn, int(s))
        
        return mn
