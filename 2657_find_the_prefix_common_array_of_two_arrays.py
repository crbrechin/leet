class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = defaultdict(int)
        total = []
        a = set()
        for i,j in zip(A,B):
            common[i] += 1
            common[j] += 1

            if common[i] >= 2:
                a.add(i)
            if common[j] >= 2:
                a.add(j)
            
            total.append(len(a))

        
        # print(f'{common}') # DEBUG
        # print(f'{total}') # DEBUG

        return total
