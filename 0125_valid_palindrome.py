class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = str.maketrans("", "", "!@#$%^&*()_+,<.>/?;:'-_=+\\\" [{]}`~") # Make a translation table
        s = s.translate(t) # Remove the characters
        s = s.lower() # Lower case
        r = s[::-1] # Reverse
        # print(s) # DEBUG
        # print(r) # DEBUG
        return s == r
