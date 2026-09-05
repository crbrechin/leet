class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0

        for i in range(n):
            # print(f'{nums[:i+1]} M: {max(nums[:i+1])}, {nums[i:]} m: {min(nums[i:])}')
            x = max(nums[:i+1]) - min(nums[i:])
            if x <= k:
                return i
        return -1
