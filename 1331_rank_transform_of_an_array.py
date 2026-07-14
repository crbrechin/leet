class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        order = list(set(arr))
        order.sort()

        hashtable = defaultdict(int)

        for i in range(len(order)):
            hashtable[order[i]] = i

        # print(f'{arr}, {order}') # DEBUG

        rank = []
        for i in arr:
            rank.append(hashtable[i] + 1)

        return rank
