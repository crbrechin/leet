class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_words = {}
        words_to_pattern = {}

        order = [p for p in pattern]
        poem = s.split()

        # print(f'{order}') # DEBUG
        # print(f'{poem}') # DEBUG

        if len(order) != len(poem):
            return False

        for i,j in zip(order, poem):
            if (i in pattern_to_words and pattern_to_words[i] != j) or(j in words_to_pattern and words_to_pattern[j] != i):
                return False
            else:
                pattern_to_words[i] = j
                words_to_pattern[j] = i

        return True
