class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        # Add the `+1` to include the number itself
        f = [x for x in range(1,max(a,b)+1) if a % x == 0 and b % x == 0]
        print(f) # DEBUG
        return len(f)
