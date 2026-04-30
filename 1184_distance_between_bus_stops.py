class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start < destination:
            w = sum(j for i,j in enumerate(distance) if start <= i < destination)
        elif start > destination:
            w = sum(j for i,j in enumerate(distance) if destination <= i < start)
        else:
            return 0
        o = sum(distance) - w # Go the other way
        # print(f'{w}') # DEBUG
        # print(f'{o}') # DEBUG
        return min(w, o)
