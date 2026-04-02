class Solution:
    def reverseBits(self, n: int) -> int:
        s = format(n, "032b") # Convert to 32-bit binary number
        
        # NOTE:
        ## Padded Binary (0Nb):
        ## Pads the output with leading zeros
        ## to a specific width N

        # print(f's: {s}, {type(s)}') # DEBUG
        r = s[::-1] # Reverse

        d = int(r, 2) # Convert back to integer
        # print(f'd: {d}') # DEBUG
        return d
