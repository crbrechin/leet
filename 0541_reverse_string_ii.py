class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start = 0
        a = ""
        for stop in range(0, len(s), 2 * k):
            # print(f'{s[stop:stop+k]}') # DEBUG
            
            a += s[stop:stop+k][::-1] + s[stop+k:stop+2*k]

        return a
