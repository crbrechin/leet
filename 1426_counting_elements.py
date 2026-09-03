class Solution:
    def countElements(self, arr: List[int]) -> int:
        a = set(arr)
        
        m = max(arr)
        
        c = 0
        
        for i in a:
            if (i + 1) in a:
                c += 1
        
        return c
