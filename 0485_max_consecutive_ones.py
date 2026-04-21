class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = ''
        for n in nums:
            s += str(n)
        # print(f's: {s}') # DEBUG

        ones = s.split('0')
        # print(f'x: {x}') # DEBUG

        m = 0

        for o in ones:
            w = len(o)
            m = max(m, w)

        return m
