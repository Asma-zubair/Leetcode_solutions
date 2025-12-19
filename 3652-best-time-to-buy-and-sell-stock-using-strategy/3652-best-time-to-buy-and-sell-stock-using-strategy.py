class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Prefix profit
        preProfit = [0] * n
        preProfit[0] = strategy[0] * prices[0]
        for i in range(1, n):
            preProfit[i] = preProfit[i - 1] + strategy[i] * prices[i]

        # Prefix prices
        prePrice = [0] * n
        prePrice[0] = prices[0]
        for i in range(1, n):
            prePrice[i] = prePrice[i - 1] + prices[i]

        ans = preProfit[-1]
        half = k // 2

        for i in range(n - k + 1):
            before = preProfit[i - 1] if i > 0 else 0
            after = preProfit[-1] - preProfit[i + k - 1] if i + k < n else 0

            sell_start = i + half
            sell_end = i + k - 1

            modified = prePrice[sell_end] - (prePrice[sell_start - 1] if sell_start > 0 else 0)
            ans = max(ans, before + modified + after)

        return ans