class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        alicetotal=sum(aliceSizes)
        bobtotal=sum(bobSizes)
        diff=( bobtotal - alicetotal)//2
        
        for x in aliceSizes:
            if x+diff in set(bobSizes):
                return [x,x+diff]
