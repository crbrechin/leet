class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s = 0

        while n:
            s += n % 10
            n //= 10

        return s
