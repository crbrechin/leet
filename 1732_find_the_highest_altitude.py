class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        i = 0
        peak = 0

        while i < len(gain):
            delta = altitudes[i] + gain[i]
            # print(f'{delta}') # DEBUG

            peak = max(peak, delta)

            altitudes.append(delta)

            i += 1

        # print(f'{altitudes}') # DEBUG

        return peak
