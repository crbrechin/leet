class Solution:
    def rotatedDigits(self, n: int) -> int:
        def rotate_int(z: int) -> bool:
            flip = {
                '2' : '5',
                '5' : '2',
                '6' : '9',
                '9' : '6'
            }
            invalid = ('3', '4', '7')
            o = ""
            for k in str(z):
                if k in invalid:
                    # print(f'Invalid') # DEBUG
                    return False
                elif k in flip:
                    o += flip[k]
                else:
                    o += k
            print(f'{o}, {z} : {int(o) != z}') # DEBUG
            return int(o) != z

        good = defaultdict(int)
        good[0] = 0

        for i in range(1,n+1):
            if rotate_int(i):
                good[i] = good[i - 1] + 1
                print(f'{good[i]}') # DEBUG
            else:
                good[i] = good[i - 1]
        # print(f'{good}') # DEBUG
        return good[n]
