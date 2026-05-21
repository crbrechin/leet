class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = 0
        hash1 = set()
        for i in arr1:
            string1 = str(i)
            # print(f'{string1}') # DEBUG
            for s in range(1,len(string1)+1):
                hash1.add(string1[:s])
        # print(f'{hash1}') # DEBUG

        for j in arr2:
            string2 = str(j)

            for s in range(1, len(string2)+1):
                check = string2[:s]
                if check in hash1:
                    prefix = max(prefix, len(check))
        
        return prefix
