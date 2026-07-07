class Solution:
    def sumAndMultiply(self, n: int) -> int:
        number = 0
        total = 0
        power = 0
        while n:
            a = n % 10
            if a != 0:
                number += a * (10 ** power)
                total += a
                power += 1
            # print(f'{a}') # DEBUG
            n //= 10
        
        return number * total
