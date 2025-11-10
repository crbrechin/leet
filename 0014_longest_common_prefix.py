class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = "" # Prefix
        strs = sorted(strs, key=len) # Shortest string
        z = 0 # placeholder counter
        for c in strs[0]: # For each character
            # Get the index
            a = True # Add the switch
            for s in strs[1:]: # Compare each
                print(f'Checking: {c}') # DEBUG
                print(f'Against: {s[z]}') # DEBUG
                if strs[0][z] != s[z]: # Nasty, but using the counter helped
                    a = False
            if a == True: # If the switch didn't fail
                p += c # add the char to the prefix
            else:
                break # Otherwise, we break
            z += 1 # increment the placeholder counter
        # print(p) # DEBUG
        return p

