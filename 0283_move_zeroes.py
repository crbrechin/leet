class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = [0] * len(nums)
        n = [i for i in nums if i != 0]
        g = [j if j else k for j,k in zip_longest(n,z)]
        # print(f'{g}') # DEBUG
        nums[:] = g
        return nums
