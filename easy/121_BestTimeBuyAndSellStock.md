# 121. Best Time to Buy and Sell Stock

[Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150)

To solve this problem, I used a two pointer approach and variables to keep track of the current profit and max profit. The buy pointer points to the zero index of the prices array, and the sell points to the 1st index. Iterate through the array and calculate the current profit each time. If the current profit is greater, update the current profit. Each iteration we always increment the sell pointer, and if the current sell price is lower than the current buy price, update the buy pointer since it's better to buy low. 

- Time complexity: O(n)
- Space complexity: O(1)


```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]
            
            # Update max profit if our current profit is greater
            if curr_profit > max_profit:
                max_profit = curr_profit
            
            # If our current buy price is greater than the sell price, update the buy pointer to buy at a lower price.
            if prices[buy] > prices[sell]:
                buy = sell

            # We always want to increment the sell pointer
            sell += 1
        
        # Once the loop finishes, we either found a profit or it is impossible to make a profit.
        return max_profit
```