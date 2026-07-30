class Solution:
    def minimumPushes(self, word: str) -> int:
        # All letters must be unique

        i, l = 0, len(word)
        presses = 0

        order = 1

        while i < l:
            presses += 1 * order
            i += 1 
            if i % 8 == 0:
                order += 1

            # print(f'L: {l}, P: {presses}') # DEBUG

        return presses
