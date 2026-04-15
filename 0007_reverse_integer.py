class Solution:
    def reverse(self, x: int) -> int:
        g = str(x)
        k = ''

        if g[0] == '-':
            h = '-'
            g = g[1:]
        else:
            h = ''
        for i in g[::-1]:
            # print(i) # DEBUG
            k += i
        
        k = h + k

        return int(k) if abs(int(k)) < 2147483647 else 0
