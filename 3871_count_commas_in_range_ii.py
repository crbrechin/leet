class Solution:
    def countCommas(self, n: int) -> int:
        ceiling = int(log10(n) // 3) + 1 # Get the 10^3 power rounded up by 1
        count = sum(max(0, n - 10 ** (3 * i) + 1) for i in range(1,ceiling))
        return count
