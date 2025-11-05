class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        sums = []
        for i in range(len(nums) - k + 1):
            s = nums[i:i+k]
            a = list(set(s))
            b = sorted(a, key= lambda n: (s.count(n), n), reverse=True)[:x] # Get the counts and then sizes
            # print(b) # DEBUG
            w = 0
            for m in b:
                # print(m) # DEBUG
                w += m * s.count(m)
            sums.append(w)
        # print(sums)
        return sums
