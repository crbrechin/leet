class Solution:
    def smallestPalindrome(self, s: str) -> str:
        ln = len(s)
        mid = ln // 2

        # print(f'{s[mid]}') # DEBUG

        a = "".join(sorted(s[:mid]))

        b = "".join(reversed(a))

        # print(f'{a}, {b}') # DEBUG

        return a + s[mid] + b if ln % 2 == 1 else a + b
