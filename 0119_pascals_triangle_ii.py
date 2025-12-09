class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Handle edge cases
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return [1,2,1]
        # For regular cases
        else: 
            o = [[1],[1,1]] # Start the first 2 rows
            for r in range(2,rowIndex+1):
                e = o[r - 1] # Look back
                f = [1] * (len(e) + 1) # Create an list [1,1,...]
                for i in range(1,len(f)-1): # Iterate through f[1:n-1]
                    f[i] = e[i-1] + e[i] # Update the values
                o.append(f) # Append the rows
        # print(o) # DEBUG
        return o[-1]
