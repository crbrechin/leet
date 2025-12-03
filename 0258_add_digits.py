class Solution:
    def addDigits(self, num: int) -> int:
        a = sum([int(i) for i in str(num)]) # Get every single integer from each decimal place
        # print(a) # DEBUG
        if len(str(a)) == 1: # If it's a single digit
            # return it
            return a
        else: # Recurse
            return self.addDigits(a)
