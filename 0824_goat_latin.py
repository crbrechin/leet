class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Split into words
        s = [w for w in sentence.split(' ')]
        o = "" # Empty sentence
        # print(s) # DEBUG
        c = 1 # Start counting at 1
        for w in s:
            # If a word begins with a vowel
            # ('a', 'e', 'i', 'o', or 'u'),
            # append "ma" to the end of the word
            # NOTE: Don't forget uppercase
            if w[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                w += "ma"
            # If a word begins with a consonant
            #(i.e., not a vowel),
            elif w[0] not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                # remove the first letter and
                # append it to the end,
                # then add "ma".
                w = w[1:] + w[0] + "ma"
            # Add one letter 'a' to the end
            #of each word per its word index in the sentence,
            # starting with 1.
            w = w + "a" * c
            # print(w) # DEBUG
            c += 1
            o += w + ' '
        o = o[:len(o) - 1] # Pop the last space
        # print(o) # DEBUG
        return o
