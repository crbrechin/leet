class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [''] * m

        for g in range(m):
            grid[g] = '#' * (n - 1) + '.'
        grid[0] = '.' * n

        # print(f'{grid}') # DEBUG

        return grid
