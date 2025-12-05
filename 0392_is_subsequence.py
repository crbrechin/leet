class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Counters
        c = 0
        d = 0

        # Loop through both strings
        while c < len(s) and d < len(t):
            if s[c] == t[d]: # If we find a match at index `c`
            # then move to the next index
                c += 1 
            d += 1
        # Do we have the same number of matches?
        return c == len(s)
