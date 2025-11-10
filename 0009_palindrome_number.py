class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        p = s[::-1]
        return p == s
