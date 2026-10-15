class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # counts = Counter(nums)

        count = 0

        for i in range(len(nums)):
            for j in range(i+1):
                count += len(set(nums[j:i+1]))**2
                # print(f'{nums[j:i+1]}') # DEBUG
        
        return count
