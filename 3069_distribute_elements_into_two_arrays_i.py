class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]

        for z in range(2, len(nums)):
            if arr2[-1] < arr1[-1]:
                arr1.append(nums[z])
            else:
                arr2.append(nums[z])

        # print(f'{arr1}') # DEBUG
        # print(f'{arr2}') # DEBUG

        out = arr1 + arr2

        return out
