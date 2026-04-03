class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        u = []
        for i, j in zip(s, t):
            if (i, j) not in u:
                u.append((i, j))
        # print(u) # DEBUG
        # We don't really care
        # to test for all instances.
        # But if there are more pairs
        # than there are unique letters,
        # we return `False`
        return len(u) == len(set(s)) and len(u) == len(set(t))
