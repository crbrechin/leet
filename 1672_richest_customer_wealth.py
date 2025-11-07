class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = [] # Declare empty array
        for a in accounts: # For every customer
            # Sum their wealth
            m.append(sum(a)) # and put it in the array
        return max(m) # Return the highest wealth
