class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        start,total,tank=0,0,0
        for i in range(len(gas)):
            total+=gas[i]-cost[i]
            tank+=gas[i]-cost[i]

            if tank<0:
                start=i+1
                tank=0
        if total>=0:
            return start
        return -1
