class Solution(object):
    def maxProfit(self, prices):
        mini=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            else:
                profit=max(profit,prices[i]-mini)
        return profit

        

