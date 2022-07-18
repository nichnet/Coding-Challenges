#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution(object):
    def addDigits(self, num):
        
        
        lastNum = str(num)
        
        
        while len(lastNum) > 1:
            sum = 0
            for i in lastNum:
                sum += int(i)
            
            lastNum = str(sum)
        
        return lastNum        
        
