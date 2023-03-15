# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        seen = []
        prices_dict = list(dict.fromkeys(prices))
        for idx in range(len(prices_dict)):
            if all([prices_dict[idx]<j for j in seen]):
                temp_profit = sorted(set(prices[prices.index(prices_dict[idx]):]),reverse=True)[0]-prices_dict[idx]
                if temp_profit>profit:
                    profit=temp_profit
            seen+=[prices_dict[idx]]
        return profit