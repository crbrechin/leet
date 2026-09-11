class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        y,z = 0,1
        squares = []
        
        for x in nums:
            y = x**2
            start,stop=0,len(squares) - 1
            while start <= stop:
                mid = start + (stop - start) // 2
                # print(f'{start} : {stop} : {mid}')
                if y > squares[mid]:
                    # Move the pointers up
                    start = mid + 1
                elif y < squares[mid]:
                    stop = mid - 1
                else:
                    # print(f'{squares}')
                    start = mid + 1
                    break
                
            squares.insert(start, y)
        
        return squares
