#!/usr/bin/python3
"""Given a pile of coins of different values, determine the fewest number
of coins needed to meet a given amount total"""


def makeChange(coins, total):
    """
    Parameters:
        coins: is a list of the values of the coins in your possession
        total: The target number
    Returns:
        fewest number of coins needed to meet total.
        If total is 0 or less, return 0
        If total cannot be met, return -1
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)   
    if dp[total] == float('inf'):
        return -1     
    return dp[total]
