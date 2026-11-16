class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            new = ""
            for i in range(0, len(s), k):
                temp = s[i:i+k]
                # print(f'{temp}') # DEBUG
                total = sum(int(c) for c in temp)
                new += str(total)
            # print(f'{new}') # DEBUG
            s = new
        return s
