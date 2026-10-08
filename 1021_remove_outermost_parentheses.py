class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out = ""

        o = 0 # Count opening
        c = 0 # Count closing
        m = 0 # Marker for start

        for i,p in enumerate(s):
            if p == '(':
                o += 1
            else:
                c += 1
            if c == o:
                out += s[m+1:i]
                # print(f'{out}') # DEBUG
                m = i + 1
                o,c = 0,0

        return out
