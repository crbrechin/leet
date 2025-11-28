class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        l = { # Memory efficient table instead of a list
            'a':1,
            'b':2,
            'c':3,
            'd':4,
            'e':5,
            'f':6,
            'g':7,
            'h':8,
        }

        # print(f"{l[coordinate1[0]]}") # DEBUG
        o = l[coordinate1[0]] # Get dictionary value
        p = l[coordinate2[0]] # Get dictionary value

        q = int(coordinate1[1]) # Convert to `int`
        r = int(coordinate2[1]) # Convert to `int`

        if o % 2 == p % 2: # Both even or both odd
            return q % 2 == r % 2 # Both even or both odd
        else:
            # Otherwise, they're different
            # Alternating row and column colours
            return q % 2 != r % 2
