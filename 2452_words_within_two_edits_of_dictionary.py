class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        results = []
        for q in queries:
            for d in dictionary:
                dif = sum(x != y for x,y in zip(q,d))

                if dif <= 2:
                    results.append(q)
                    break
        
        return results
