class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = d = 0
        e = ""

        while c <= len(s) - 1 and d <= len(t) - 1:    
            
            if s[c] == t[d]:
                e += t[d]
                # Next char
                c += 1
                d += 1
            else:
                d += 1
        
        # print(f'{e}') # DEBUG

        return e == s
            
