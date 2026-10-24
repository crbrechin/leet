class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        z = 3
        i = -1
        while z < n:
            i += 1
            z = 3 ** i
        
        # print(f'{z}**{i}') # DEBUG

        return z == n
