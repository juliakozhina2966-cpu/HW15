"""This file defines the function for the most efficient cuts."""


def rod_cutting(prices, n):
    """Return the the best rod cutting."""
    dp = [0] * (n + 1)
    cut = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            if j <= len(prices):
                if prices[j - 1] + dp[i - j] > max_val:
                    max_val = prices[j - 1] + dp[i - j]
                    cut[i] = j
        dp[i] = max_val

    res = []
    length = n
    while length > 0:
        res.append(cut[length])
        length -= cut[length]

    return res, dp[n]
