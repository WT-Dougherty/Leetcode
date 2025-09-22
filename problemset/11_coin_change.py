"""
Problem: Coin Change (DP - Unbounded)
-------------------------------------
Given coins of denominations `coins` and a total `amount`, return the fewest number of coins needed to make up that amount.
Return -1 if the amount cannot be made up.

Approach (Bottom-up DP):
- dp[a] = min(dp[a], dp[a - coin] + 1) for each coin.
- Initialize dp[0] = 0 and others to INF.

Time: O(amount * len(coins)) | Space: O(amount)
"""
from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    INF = amount + 1
    dp = [INF]*(amount+1)
    dp[0] = 0
    for a in range(1, amount+1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], dp[a-c] + 1)
    return dp[amount] if dp[amount] != INF else -1

def _test():
    assert coin_change([1,2,5], 11) == 3  # 5+5+1
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([2,5,10,1], 27) == 4  # 10+10+5+2

if __name__ == "__main__":
    _test()
    print("OK")