class Solution:
    def processStr(self, s: str) -> str:
        result = ''
        for i,c in enumerate(s):
            if c == '*':
                # print('*') # DEBUG
                if len(result) > 0:
                    result = result[:-1]
            elif c == '#':
                # print('#') # DEBUG
                result += result
            elif c == '%':
                # print('%') # DEBUG
                result = result[::-1]
            else:
                result += c
        return result
