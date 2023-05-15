from typing import List
import random


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        left, right = 0, 1
        while right < len(prices):
            currProfit = prices[right] - prices[left]
            maxProfit = max(currProfit, maxProfit)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return maxProfit


def main():
    s = Solution()

    # Test loop
    for i in range(10):
        prices = [random.randrange(0, 15) for _ in range(10)]
        print(f"{i}: {prices}")
        print(f"max profit: {s.maxProfit(prices)}\n")


main()
