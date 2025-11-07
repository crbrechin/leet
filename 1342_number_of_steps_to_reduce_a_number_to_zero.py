class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0 # Start the counter
        while num > 0: # As long as `num > 0`
            if num % 2 == 0: # `num` is even
                num = num / 2
            else: # Otherwise `num` is odd
                num -= 1
            c += 1 # Increase the counter
        return c
