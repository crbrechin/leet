class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            l = log(n, 4)
            return l == round(l)
