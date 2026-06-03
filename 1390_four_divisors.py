class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        factors = defaultdict(set)
        
        for n in nums:
            i = 1
            while i <= sqrt(n):
                x = n / i
                if int(x) == x and int(x) not in factors[n]:
                    factors[n].add(i)
                    factors[n].add(int(x))
                i += 1
        
        # print(f'{factors}') # DEBUG
        fours = 0
        for p in nums:
            if len(factors[p]) == 4:
                for i in factors[p]:
                    fours += i
           

        return fours
