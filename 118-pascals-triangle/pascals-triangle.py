class Solution(object):
    def generate(self, numRows):
        res=[]
        for i in range(numRows):
            row=[]
            for j in range(i+1):
                if j ==0 or j==i:
                    row.append(1)
                else:
                    val=res[i-1][j-1]+res[i-1][j]
                    row.append(val)
            res.append(row)
        return res