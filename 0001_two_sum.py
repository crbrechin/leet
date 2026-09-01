class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = defaultdict(list)
        
        for i,z in enumerate(nums):
            complement = target - z
            # print(f'{i}, {z}') # DEBUG
            
            n[z].append(i)

            if complement == z:
                if len(n[complement]) == 2:
                    return [n[z][0], n[z][1]]
            elif complement in n and complement != z:
                return [n[z][0], n[complement][0]]

        # print(f'{n}') # DEBUG
