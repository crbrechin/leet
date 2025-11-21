class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        t = []
        for i in range(len(nums) - k + 1):
            s = nums[i:i+k] # Substring
            a = list(set(s)) # Unique
            a = sorted(a, key= lambda n: (s.count(n), n), reverse=True)[:x] # Get the counts and then sizes
            # print(a) # DEBUG
            w = sum([i * s.count(i) for i in a]) # Sum the most frequent in the substring
            # print(w) # DEBUG
            t.append(w)
        # print(t) # DEBUG
        return t
