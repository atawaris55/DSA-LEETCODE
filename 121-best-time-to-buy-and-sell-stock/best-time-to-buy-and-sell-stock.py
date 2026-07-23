class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]<mini:
                mini=prices[i]
            else:
                profit=max(profit,prices[i]-mini)
        return profit

        

