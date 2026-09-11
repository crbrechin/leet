class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        even = set()
        
        for i,j,k in permutations(digits, 3):
            
            d = i * 100 + j * 10 + k

            # print(f'{i}{j}{k}') # DEBUG
            if d % 2 == 0 and d >= 100:
                # print(f'{d}') # DEBUG
                even.add(d)

        
        return len(even)
