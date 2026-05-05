class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        counts = defaultdict(int)
        
        
        words = [w for w in re.findall(r'\b\w+\b', paragraph.lower()) if w not in banned]
        for w in words:
            counts[w] += 1
        
        highest = max(counts, key=counts.get)
        
        # print(f'{counts}') # DEBUG
        # print(f'{highest}') # DEBUG

        return highest
