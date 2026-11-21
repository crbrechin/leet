class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(x: int) -> int:
            numbers = []
            while x:
                a = x % 10
                x //= 10
                numbers.append(a)
            
            output = 0
            power = 0
            for z in numbers[::-1]:
                output += z * 10 ** power
                power += 1

            return output
        
        return abs(n - reverse(n))
            
