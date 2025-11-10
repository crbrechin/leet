class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = [] # Empty list
        for e in range(1,n + 1):
            s = "" # Empty string
            if e % 3 == 0: # Divisible by 3
                s += "Fizz"
            if e % 5 == 0: # Divisible by 5
                s += "Buzz"
            if s: # `s` not empty
                l.append(s)
            else:
                l.append(str(e)) # Stringify it
        # print(l) # DEBUG
        return l
