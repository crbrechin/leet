class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = sorted([i for i in s])
        # print(u) # DEBUG
        v = sorted([j for j in t])
        # print(v) # DEBUG
        return u == v
