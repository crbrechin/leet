class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        a = []
        for row in grid:
            for column in row:
                a.append(column) # Distance
        # print(f'{a}') # DEBUG
        d = [c % x for c in a]
        # print(f'{d}') # DEBUG
        if len(set(d)) > 1:
            return -1
        else:
            a.sort()
            ops = 0

            # mo = mode(a)
            # me = mean(a)
            # mi = min(a)
            # ma = max(a)
            # print(f'{mo}, {me}, {mi}, {ma}') # DEBUG

            m = a[len(a)//2]

            ops = sum(abs(e - m)//x for e in a)
            # print(f'{ops}') # DEBUG

            return ops
