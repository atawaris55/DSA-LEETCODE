class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        alicetotal=sum(aliceSizes)
        bobtotal=sum(bobSizes)
        diff=( bobtotal - alicetotal)//2
        bobset=set(bobSizes)
        for x in aliceSizes:
            if x+diff in bobset:
                return [x,x+diff]
