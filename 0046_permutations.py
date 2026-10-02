class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backTrack(current: list):
            if len(current) == len(nums): # If a leaf-node
                answer.append(current[:]) # Add a copy to `answer`
            
            for n in nums:
                if n not in current: # If `n` hasn't been used
                    current.append(n) # Add it to the list
                    backTrack(current) # Look for new `n` to add from `nums`
                    current.pop() # Remove the last `n` from `current`
        
        answer = []
        backTrack([])

        return answer
