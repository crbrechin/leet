class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # print(f'{26*26}') # DEBUG # AA: 676
        # print(f'{((1) * (26**2)) + ((2) * (26**1)) + ((3) * (26**0))}') # DEBUG # ABC: 731
        # A : 1
        # AA : 27 = 26^1 + 26^0
        # AAA : 703 = 26^2 + 26^1 + 26^0
        # AAZ : 728 = (1) * 26^2 + (1) * 26^1 + (26) * 26^0
        # ABC : 731 = (1) * 26^2 + (2) * 26^1 + (3) * 26^0

        c = 0 # Total

        for i,z in enumerate(columnTitle[::-1]): # Go backwards for significance
            c += (ord(z) - 64) * (26**i) # ord('A') = 64
            # print(f'{i}, {c}') # DEBUG

        # print(c) # DEBUG
        return c
