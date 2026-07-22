class Solution:
    def binaryGap(self, n: int) -> int:
        delta = 0
        last,previous = 0,0

        # print(f'{str(bin(n))[2:]}') # DEBUG

        for i,e in enumerate(str(bin(n)[2:])):
            
            # print(f'{e} : {last} - {previous} = {last - previous}: {delta}') # DEBUG
            if e == '1':
                previous = last
                last = i
                delta = max(delta, last - previous)
        
        return delta
