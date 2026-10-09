class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)
        
        return all(r[x] <= m[x] for x in r)
