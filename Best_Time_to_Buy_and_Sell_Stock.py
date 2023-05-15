class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # buy_price = prices[0]
        # buy_at = 0
        # sell_price = prices[0]
        # sell_at = len(prices) - 1
        # for idx, price in enumerate(prices):
        #     if idx != 0:
        #         if price < buy_price:
        #             if (max(prices[idx: len(prices)]) - price) > (sell_price - buy_price):
        #                 buy_price = sell_price = price
        #                 buy_at = sell_at = idx
        #         elif price > sell_price and idx > buy_at:
        #             sell_price = price
        #             sell_at = idx
        #
        # return sell_price - buy_price

        profit = 0
        buy_price = prices[0]

        for idx,price in enumerate(prices):
            if idx != 0:
                buy_price = min(buy_price,price)
                profit = max(profit, price - buy_price)
        return profit




Obj = Solution()
print(Obj.maxProfit([3,2,6,5,0,3]))
