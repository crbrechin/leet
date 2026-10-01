class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'[', '(', '{'}
        closing = {'[':']', '(':')', '{':'}'}

        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif closing[stack[-1]] != c:
                return False
            else:
                # print(f'{c}') # DEBUG
                stack.pop(-1)
        
        return len(stack) == 0
