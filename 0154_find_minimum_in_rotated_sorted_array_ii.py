class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2

        while left < right:
            mid = left + (right - left) // 2
            
            # print(f'({left},{nums[left]}):({mid},{nums[mid]}):({right},{nums[right]})') # DEBUG

            if nums[left] == nums[right]:
                left += 1
            elif nums[left] > nums[mid]:
                right = mid
            elif nums[right] < nums[mid]:
                left = mid + 1
            else:
                break

        # print(f'({left},{nums[left]}):({mid},{nums[mid]}):({right},{nums[right]})') # DEBUG
        return nums[left]
        
