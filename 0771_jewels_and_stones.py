class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = Counter(stones)
        
        count = 0
        for j in jewels:
            count += s[j]
        
        return count
