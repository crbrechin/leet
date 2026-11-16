class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # print(f'{x ^ y}') # DEBUG
        return sum(1 for i in str(bin(x ^ y)) if i == '1')
