class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        u = list(set(nums))
        t = sorted(u, key = lambda n: nums.count(n), reverse = True)[:2]
        return t
