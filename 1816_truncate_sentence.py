class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(word for word in s.split(" ")[:k])
