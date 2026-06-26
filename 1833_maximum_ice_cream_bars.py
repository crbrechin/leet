class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        eaten = 0
        
        # A frequency table
        stock = [0] * (max(costs) + 1)

        # Count the frequencies
        for i in costs:
            stock[i] += 1
        
        # Eat the icecream
        for c in range(len(stock)):
            while stock[c] > 0 and coins >= c:
                # print(f'${c}, In Stock: {stock[c]}') # DEBUG
                stock[c] -= 1 # Remove inventory
                # print(f'Coins: ${coins}') # DEBUG
                coins -= c # Pay
              
                eaten += 1 # Eat
                # print(f'Eaten: {eaten}') # DEBUG
        
        return eaten # You lil fatty...
