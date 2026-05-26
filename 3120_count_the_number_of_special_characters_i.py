class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
                
        uppers = set()
        lowers = set()
        specials = set()

        # ord('A'): 65

        for w in word:
            o = ord(w) - 65
            if o < 32: # Uppercase
                uppers.add(o)
            else: # Lowercase
                lowers.add(o)
        
        for l in lowers:
            if l - 32 in uppers:
                specials.add(l)
        
        
        # print(f'{uppers}') # DEBUG
        # print(f'{specials}') # DEBUG

        return len(specials)

        # O(n + m), where m = len(lowers)
