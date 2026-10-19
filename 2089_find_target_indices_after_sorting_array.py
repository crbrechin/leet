class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        start,stop = 0,0
        for n in nums:
            if n < target:
                start += 1
            elif n == target:
                stop += 1
        # print(f'{start}, {stop}') # DEBUG
        return [i for i in range(start, start + stop)]
