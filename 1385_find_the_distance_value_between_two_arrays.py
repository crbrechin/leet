class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        l = len(arr2)
        arr2.sort()
        count = 0
        for z in arr1:
            i = 0
            while i < l and abs(z - arr2[i]) > d:
                # print(f'abs({z} - {arr2[i]}) = {abs(z - arr2[i])} > {d}') # DEBUG
                i += 1
            if l - i == 0:
                count += 1
            # print(f'{l} - {i} = {l - i}') # DEBUG

        return count
