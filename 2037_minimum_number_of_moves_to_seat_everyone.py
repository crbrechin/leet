class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        return sum(abs(s - d) for s, d in zip(sorted(seats), sorted(students)))
