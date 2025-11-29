class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        e = 0
        a = []
        for i in str(n)[::-1]:
            # print(f"{i}") # DEBUG
            if i == '0': # Skip over the zero
                next
            else:
                # a.insert(0, int(i) * 10 ** e) # Takes a long time
                a.append(int(i) * 10 ** e)
            e += 1
        # Reverse it, method for speed
        a = a[::-1]
        # print(a) # DEBUG
        return a
