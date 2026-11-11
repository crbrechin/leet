class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        overallCost = 0

        bothNeeded = min(need1, need2)

        if costBoth < cost1 + cost2:
            overallCost += costBoth * bothNeeded
            need1 -= bothNeeded
            need2 -= bothNeeded

        if need1 > 0:
            overallCost += min(costBoth, cost1) * need1
        if need2 > 0:
            overallCost += min(costBoth, cost2) * need2
        
        return overallCost
