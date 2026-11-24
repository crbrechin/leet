class Solution:
    def maxLength(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return 2

        j = 1
        product_equivalent = 0

        for i in range(len(nums) - 1):
            while j < len(nums):
                if math.prod(nums[i:j]) == math.lcm(*nums[i:j]) * math.gcd(*nums[i:j]):
                    product_equivalent = max(product_equivalent, len(nums[i:j]))
                j += 1
            j = i + 1

        j = len(nums) - 1

        for i in range(len(nums), 0, -1):
            # print(f'{i}') # DEBUG
            while j >= 0:
                if math.prod(nums[j:i]) == math.lcm(*nums[j:i]) * math.gcd(*nums[j:i]):
                    product_equivalent = max(product_equivalent, len(nums[j:i]))
                j -= 1
            j = i - 1

        return product_equivalent
