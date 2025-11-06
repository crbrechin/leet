class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        s = []
        for n in nums:
            sum += n
            s.append(sum)
        return s
