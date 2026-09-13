class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'

        d = []
        sign = '-' if num < 0 else ''
        n = abs(num)
        while n > 0:
            d.append(str(n % 7))
            n //= 7
            
        return sign + ''.join(reversed(d))
