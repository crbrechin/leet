class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        n = nums # Non-destructive
        u = max(n) # Get the max
        i = n.index(u) # Get the index
        # print(f"{u},{i}") # DEBUG
        n.pop(i) # Pop it from the list
        v = max(n) # Get the second max
        w = min(n) # Get the min

        return u + v - w
