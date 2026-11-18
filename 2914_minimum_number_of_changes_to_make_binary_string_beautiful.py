class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(0, len(s), 2):
            sub = s[i:i+2]
            # print(f'{i}, {sub}') # DEBUG
            chars = Counter(sub)
            if chars["0"] == 1:
                count += 1

        return count
