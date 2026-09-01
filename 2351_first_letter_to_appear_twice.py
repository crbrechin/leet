class Solution:
    def repeatedCharacter(self, s: str) -> str:
        a = defaultdict(int)
        for c in s:
            a[c] += 1
            if a[c] == 2:
                return c
