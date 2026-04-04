class Solution:
    def climbStairs(self, n: int) -> int:
        # Source: https://www.youtube.com/watch?v=Y0lT9Fck7qI
        one = 1
        two = 1
        # Fibonacci sequence
        for i in range(0, n - 1):
            temp = one # Temporary
            one = one + two
            two = temp
            print(f"Temp: {temp}, One: {one}, Two: {two}") # DEBUG
        return one
