class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        start = 0
        stop2 = stop1 = len(colors) - 1

        while start != stop1 and colors[start] == colors[stop1]:
            stop1 -= 1

        sroloc = colors[::-1]

        while start != stop2 and sroloc[start] == sroloc[stop2]:
            stop2 -= 1

        return max(stop1 - start, stop2 - start)
