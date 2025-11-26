class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        q = 0
        for x,c in zip(digits,range(len(digits))):
            q += x * 10 ** (len(digits) - c - 1) # Add the digit in the proper place
            # print(f"{x}, {c}, {q}") # DEBUG
        q += 1 # Increment by 1
        q = str(q) # Convert to string for easy iteration
        d = [int(i) for i in q] # Add back to an array
        # print(d) # DEBUG
        return d
