class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        letters = defaultdict(list)
        specials = set()
        for i,w in enumerate(word):
            letters[w].append(i)

        # print(f'{letters}') # DEBUG
        # print(f'{ord('A')}') # 65
        
        for z in range(26):
            lower = chr(z + 65 + 32)
            upper = chr(z + 65)
            # print(f'{lower}:{letters[lower]}, {upper}:{letters[upper]}') # DEBUG
            if upper not in letters or lower not in letters:
                continue
            
            elif all(x - letters[upper][0] < 0 for x in letters[lower]):
                # print('DEBUG') # DEBUG
                specials.add(lower)

        # print(f'{specials}') # DEBUG

        return len(specials)
