class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if all(i % 2 == 0 for i in nums1) or all(i % 2 == 1 for i in nums1):
            return True
        else:
            m = min([i for i in nums1 if i % 2 == 1])
            if all(i > m for i in nums1 if i % 2 == 0):
                return True
            else:
                return False
