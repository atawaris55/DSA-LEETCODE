class Solution(object):
    def calPoints(self, operations):
        record=[]
        total=0
        for i in operations:
            if i  =='C':
                record.pop()
            elif i =='D':
                record.append(2*record[-1])
            elif i == '+':
                record.append(record[-1]+record[-2])
            else:
                record.append(int(i))
        for i in record:
            total+=i
        return total
        


