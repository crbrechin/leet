class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        translation = ""
        a = ord('a')
        for word in words:
            x = 0
            for char in word:
                x += weights[ord(char) - a]
                # print(f'{x}') # DEBUG
            
            t = x % 26

            translation += chr(26 - t + a - 1)

        return translation
