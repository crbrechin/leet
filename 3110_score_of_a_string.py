class Solution:
    def scoreOfString(self, s: str) -> int:
        a = ord(s[0])
        score = 0

        for char in s[1:]:
            o = ord(char)
            # print(f'{o}') # DEBUG
            score += abs(a - o)
            a = o
        return score
