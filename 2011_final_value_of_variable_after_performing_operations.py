class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        sums = Counter(operations)

        return sums["X++"] + sums["++X"] - sums["X--"] - sums["--X"]
