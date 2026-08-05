class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ln = len(nums)

        if k == 0:
            return nums
        if ln < k:
            return [-1] * ln
        

        s = 0

        averages = [0]
        for i in nums:
            s += i
            averages.append(s)
        

        subarray = [(averages[i + k + 1] - averages[i - k]) // (2 * k + 1) if i in range(k, ln - k) else -1 for i in range(0, ln)]

        # for i in range(k, ln - k):
        #     print(f'{i - k}, {i}, {i + k}') # DEBUG
        #     print(f'{averages[i + k + 1] - averages[i - k]}, {nums[i - k: i + k + 1]}') # DEBUG

        # return [0]
        return subarray
