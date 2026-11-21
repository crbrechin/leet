class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        output = 0
        for z in range(n + 1):
            if z % m == 0:
                output -= z
            else:
                output += z
        return output
