class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        start = 0
        mx = 0

        freq = Counter()

        # print(f'{freq}') # DEBUG

        for stop in range(len(s)):
            freq[s[stop]] += 1
            
            while freq[s[stop]] > 2:
                freq[s[start]] -= 1
                start += 1
            
            mx = max(mx, stop - start + 1)


        return mx
