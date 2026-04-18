class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        r = ""
        o = ""
        for a in s:
            if a.isalpha():
                r = a + r
                # print(f'{a} : {r}') # DEBUG
        for z in s:
            if z.isalpha():
                o += r[0]
                r = r[1:]
                # print(f'{z}') # DEBUG
            else:
                o += z
        print(f'{o}') # DEBUG
        return o
