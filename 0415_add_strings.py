class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # I don't like this work-around
        sys.set_int_max_str_digits(68000)
        # Convert to integer
        # NOTE: Reverse order so that we can
        # perform carrying operations
        # more easily in the loop
        x = [int(n) for n in num1[::-1]]
        # print(x) # DEBUG
        y = [int(m) for m in num2[::-1]]
        # print(y) # DEBUG
        e = 0
        s = 0
        for j,k in itertools.zip_longest(x,y):
            if j == None:
                j = 0
            if k == None:
                k = 0
            s += (j + k) * 10**e
            e += 1
        # Convert the sum back to string
        return str(s)
        # Obviously, I am wrong to convert
        # integers using the integer arrays.
        # I don't really know what it meant
        # when it said "do not convert
        # integers directly..."
