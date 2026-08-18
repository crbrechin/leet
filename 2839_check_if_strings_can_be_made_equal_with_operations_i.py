class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1Odd, s1Even = [], []
        s2Odd, s2Even = [], []
        
        for i,z in enumerate(zip(s1, s2)):
            j = z[0]
            k = z[1]
            if i % 2 == 0:
                s1Even.append(j)
                s2Even.append(k)
            else:
                s1Odd.append(j)
                s2Odd.append(k)
        
        return sorted(s1Odd) == sorted(s2Odd) and sorted(s1Even) == sorted(s2Even)
