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
    i = 0
    count = 0

    coins.sort(reverse=True)
    while total > 0 and i < len(coins):
        if coins[i] <= total:
            count += total // coins[i]
            total %= coins[i]
        i += 1
    return count if total <= 0 else -1
