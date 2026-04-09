class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_n(q: int) -> int:
            a = str(q)
            return sum([int(i)**2 for i in a])

        v = []
        b = n

        while True:
            print(f'{b} : {v}') # DEBUG
            b = sum_n(b)
            if b == 1:
                return True
            elif b in v: # We have already looped through the number
                return False
            else:
                v.append(b) # Add to list of seen numbers
