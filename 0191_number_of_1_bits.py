class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:] # Binarize
        k = 0 # Counter
        for e in b:
            if e == "1":
                k += 1
        return k
