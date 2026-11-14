class Solution(object):
    def smallestEvenMultiple(self, n):
        for i in range(2,(n*10)+1):
            if i%n==0 and i%2==0:
                return i
