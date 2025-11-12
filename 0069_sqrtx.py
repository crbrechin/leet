class Solution:
    def mySqrt(self, x: int) -> int:
        z = 0 # Declare a counter
        while z * z <= x: # Test the condition first
            z += 1 # Increment
            # 0,1,2,3
        return z - 1 # We over count by 1 which aborts the loop

# The problem requires me to solve without using built-ins.
# The real solution: `return floor(sqrt(x))`
