class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        stack = [0] * len('balloon')
        count = 0
        
        for char in text:
            if char == 'b':
                stack[0] += 1
            elif char == 'a':
                stack[1] += 1
            elif char == 'n':
                stack[6] += 1
            elif char == 'l':
                if stack[2] >= stack[3]:
                    stack[3] += 1
                else:
                    stack[2] += 1
            elif char == 'o':
                if stack[4] >= stack[5]:
                    stack[5] += 1
                else:
                    stack[4] += 1
            print(f'{stack}')
            if all(i >= 1 for i in stack):
                count += 1
                stack[:] = [x - 1 for x in stack]
        
        return count
