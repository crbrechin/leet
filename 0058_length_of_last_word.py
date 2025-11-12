class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = [word for word in s.split(" ")] # Split the words up into an array
        w = [word for word in filter(None, w)] # Remove the empty
        return len(w[-1])
