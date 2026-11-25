# 121 Best Time to Buy and Sell Stock (easy)

"""
Given prices array -> each index is the price of the stock given the ith day

Profit is future day - previous day

Return the max profit we can get?

Ex: [7,1,5,3,5,4] -> 5 b/c 7-5
"""


# Brute force with checking every possible combo
def a(prices):
    max_value = float("-inf")
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > max_value:
                max_value = prices[j] - prices[i]
    return max_value


# What if we can do a sliding window try?
def b(prices):
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP


"""
Attempt 2 

Given: 
prices int array where price[i] is the stock on i day 
Find the best profit where we buy and then sell
Basically find the pair that gives best j - i 

"""
