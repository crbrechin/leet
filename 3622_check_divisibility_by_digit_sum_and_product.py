class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        a = n

        while n:
            z = n % 10
            s += z
            p *= z
            n //= 10

        # print(f'{a} % ({s} + {p}) = {a % (p + s)}') # DEBUG



        return a % (p + s) == 0
