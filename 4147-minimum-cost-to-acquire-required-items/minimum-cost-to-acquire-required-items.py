class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        common=min(need1,need2)
        ans=common*min(costBoth,cost1+cost2)
        if need1>need2:
            ans+=(need1-need2)*min(cost1,costBoth )
        else:
            ans+=(need2-need1)*min(cost2,costBoth )
        return ans
