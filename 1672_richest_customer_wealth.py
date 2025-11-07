class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = []
        for a in accounts:
            m.append(sum(a))
        return max(m)
