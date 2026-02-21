class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def convert_to_decimal(s):
            o = 0 # Output string
            i = 0 # Counter
            for x in s[::-1]:
                # Boolean
                if x == "0":
                    t = 0
                else:
                    t = 1
                # Addition
                o += 2**i * t
                i += 1
            return o

        def convert_to_binary(z):
            if z == 0: # Edge case
                return "0"
            i = 0 # Power
            while(2**i <= z): # Find the number of bits required
                i+=1
            c = [0] * i # Declare a blank string
            # print(c) # DEBUG
            s = ""
            for e in range(len(c) - 1, -1, -1): # Count down
                if z >= 2 ** e:
                    s += "1"
                    z -= 2 ** e # Decrement
                else:
                    s += "0"
            # print(s) # DEBUG
            return s
        q = convert_to_decimal(a) + convert_to_decimal(b)
        return convert_to_binary(q)
            
