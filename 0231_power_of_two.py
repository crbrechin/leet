class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False # 0 is not a multiple of 2
        elif n == 1: # If we have reduced it down to 1
            return True
        elif n % 2 != 0: # If it's odd, False
            return False
        else:
            return self.isPowerOfTwo(n/2) # Otherwise, recurse
