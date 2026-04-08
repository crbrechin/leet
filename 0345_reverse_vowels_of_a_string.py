class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        o = ""
        x = [] # Array of vowels
        for i in s:
            if i in vowels: # If it's a vowel, add it
                x.append(i)
        
        y = x[::-1] # Reverse the list

        w = 0
        for j in s:
            if j in vowels:
                o += y[w]
                w += 1
            else:
                o += j

        return o
