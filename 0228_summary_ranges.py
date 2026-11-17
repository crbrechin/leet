class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        nums[:] = [float("-inf")] + nums + [float("inf")]
        output = []
        a = ""

        for j in range(1, len(nums) - 1):
            i,k = j - 1, j + 1
            b = "" 
            if nums[i] + 1 == nums[j] and nums[j] + 1 == nums[k]:
                ...
            elif nums[i] + 1 == nums[j] and nums[j] + 1 != nums[k]:
                temp = f"{a}->{nums[j]}"
                output.append(temp)
            elif nums[i] + 1 != nums[j] and nums[j] + 1 != nums[k]:
                temp = f'{nums[j]}'
                output.append(temp)
            elif nums[i] + 1 != nums[j] and nums[j] + 1 == nums[k]:
                a = f'{nums[j]}'

        # print(f'{output}') # DEBUG
        return output
