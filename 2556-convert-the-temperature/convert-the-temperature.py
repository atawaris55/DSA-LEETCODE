class Solution(object):
    def convertTemperature(self, celsius):
        res=[]
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        res.append(Kelvin)
        res.append(Fahrenheit)
        return res

 
