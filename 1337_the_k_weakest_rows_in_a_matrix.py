class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rowStrength = defaultdict(int)
        for i,row in enumerate(mat):
            for c in row:
                if c == 1:
                    rowStrength[i] += 1
                else:
                    rowStrength[i] += 0 # Account for empty rows
        
        # print(f'{rowStrength}') # DEBUG

        weakest = [i for i,j in sorted(rowStrength.items(), key=lambda k_v: k_v[1])[:k][:]]

        return weakest
