class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i + 1) * (26 - (ord(c) - ord('a'))) for i,c in enumerate(s))
