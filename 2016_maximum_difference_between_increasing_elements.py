class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        m = -1 # Placeholder for max
        for n in range(0,len(nums)):
            # We use a for loop
            # Instead of combinations()
            # Because index_x < index_y
            for u in range(n + 1, len(nums)): # Start counting for the n + 1 
                # There are definitely some extraneous cases
                if nums[u] < nums[n]:
                    next # Because it can't possibly be bigger with a smaller integer
                elif nums[u] == nums[n]:
                    next
                elif nums[u] - nums[n] > m:
                    m = nums[u] - nums[n]
                else:
                    ... # Do nothing
                # print(m) # DEBUG
        return m
