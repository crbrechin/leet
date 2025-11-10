class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        o = [] # Output list
        # Loop through the combinations
        # until we find one that matches our target sum
        for x,y in combinations(nums, 2):
            if x + y == target: # Only one valid answer exists -- phew!

                # We want the index, not the value
                i = nums.index(x)
                o.append(i)

                # x == y creates a doubled index
                if x == y:
                    j = nums.index(y, i + 1)
                else:
                    j = nums.index(y)
                o.append(j)
        # print(o) # DEBUG
        return o
