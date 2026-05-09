class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = {
            'a' : ".-",
            'b' : "-...",
            'c' : "-.-.",
            'd' : "-..",
            'e' : ".",
            'f' : "..-.",
            'g' : "--.",
            'h' : "....",
            'i' : "..",
            'j' : ".---",
            'k' : "-.-",
            'l' : ".-..",
            'm' : "--",
            'n' : "-.",
            'o' : "---",
            'p' : ".--.",
            'q' : "--.-",
            'r' : ".-.",
            's' : "...",
            't' : "-",
            'u' : "..-",
            'v' : "...-",
            'w' : ".--",
            'x' : "-..-",
            'y' : "-.--",
            'z' : "--.."
        }

        transformations = set()
        for w in words:
            s = ""
            for c in w:
                s += morse[c]
            transformations.add(s)
        
        # print(f'{transformations}') # DEBUG

        return len(transformations)
