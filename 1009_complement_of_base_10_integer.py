class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        # print(f'{str(bin(n))}') # DEBUG

        a = ''.join('0' if i == '1' else '1' for i in str(bin(n))[2:])

        return int(a, 2)
