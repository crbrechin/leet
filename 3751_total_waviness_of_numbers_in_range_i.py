class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for num in range(num1, num2 + 1):
            # print(f'{num}') # DEBUG
            if num <= 100:
                continue
            else:
                i = num % 10
                num //= 10
                j = num % 10
                num //= 10
                k = num % 10
                num //= 10
                if (j < k and j < i) or (j > k and j > i):
                    waviness += 1
                while num:
                    i,j,k = j,k,num % 10
                    if (j < k and j < i) or (j > k and j > i):
                        waviness += 1
                    num //= 10
        return waviness
