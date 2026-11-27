class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join(format(int(w), 'b') for w in date.split('-'))
