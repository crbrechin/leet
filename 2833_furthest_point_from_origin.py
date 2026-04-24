class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = moves.count('L')
        right = moves.count('R')
        z = 'L' if left > right else 'R'
        
        # print(f'{z}') # DEBUG
        d = 0
        f = 0
        for m in moves:
            if m == '_' or m == z:
                d += 1
            else:
                f += 1
        return abs(d - f)
