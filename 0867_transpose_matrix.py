class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        return [list(col) for col in zip(*matrix)]
