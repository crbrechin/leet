class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = Counter()
        losers = Counter()
        
        for m in matches:
            winners[m[0]] += 1
            losers[m[1]] += 1
        
        only,single = [w for w in winners if w not in losers], [l for l in losers if losers[l] == 1]

        answer = [sorted(only), sorted(single)]
        
        return answer
