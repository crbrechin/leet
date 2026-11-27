class Solution:
    def maxFreqSum(self, s: str) -> int:
        v = {'a', 'e', 'i', 'o', 'u'}

        vowels, consonants = [0] * 26, [0] * 26

        for char in s:
            o = ord(char) - ord('a')
            if char in v:
                vowels[o] += 1
            else:
                consonants[o] += 1
        
        return max(vowels) + max(consonants)
