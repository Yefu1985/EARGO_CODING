# This is the coding for estimating the maximum profit from the prices list.
# I tried to keep the prices to be flexible, so it can be of any length, not only 10.
# The maximum profit can be obtained from the prices[sellDate] - prices[buyDate], and the buyDate should happen
# before sellDate.
# So, I traversed the list of prices, and update the lowest prices (minPre) before the current date.
# At the same time, I keep updating the maximum profit (maxProfit) by evaluating max(prices[i]-preMin, maxProfit).

# The time complexity for this problem is o(n), where n is the length of the prices.
# The space complexity for this problem is o(1), only a few variables are used here: premMin, maxProfit, buyDate,
# sellDate.

# For running the code, please change the prices list in line 28. The code result will show you the best buy and sell
#  date and maximum profit corresponding to the input prices.
def profit(prices):
    if len(prices) <= 1:            # Corner case, if the price list has fewer than 1 day price, then return null,null,0
        return None, None, 0    # Here are the buyDate, sellDate, and maximum profit;
    preMin, maxProfit = prices[0], 0 # preMin is the lowest price before day i; initialize it as the price on day 1;
    # maxProfi initialized as 0 (no profit)
    buyDate, sellDate = 0, 0    # Initialize the buy and sell date to be 0
    for i in range(1, len(prices)): # Traverse the prices list, and update the preMin and maxProfit
        if prices[i] < preMin:
            preMin = prices[i]
            buyDate = i+1
        if prices[i] - preMin > maxProfit:
            sellDate = i+1
            maxProfit = prices[i]-preMin
    return buyDate, sellDate, maxProfit

prices = [3, 8, 8, 55, 38, 1, 7, 42, 54, 53]    # Input for the function, the list of price
buyDate, sellDate, maxProfit = profit(prices)
print("The possible maximum profit for stock would be buying on day", buyDate, "and sell on the day", sellDate)
print("The possible maximum profit for the stock would be", maxProfit)