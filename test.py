from typing import List

def maxProfit( prices: List[int]) -> int:
    profit = 0
    pre = prices[0]
    
    for price in prices[1:]:
        if price > pre:
            print(price, pre)
            profit += price
        pre = price
    return profit

maxProfit([7,1,5,3,6,4])

