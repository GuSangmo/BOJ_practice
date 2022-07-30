from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maximum = -1e9
        minimum = 1e9
        
        for price in prices:
            #Change maximum or minimum.
            if price>=maximum : maximum = price 
            if price<=minimum : minimum = price 
            
            #if you get local minimum, and current value is higher than it, it's new candidate!
            if price > minimum:
	            profit = max(price- minimum, profit)
        return profit
