#Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:
# -  Starting with any positive integer, replace the number by the sum of the squares of its digits.
# -  Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# -  Those numbers for which this process ends in 1 are happy.

#Return true if n is a happy number, and false if not.

class Solution(object):
    def isHappy(self, n):
        num = n

        used = []
        
        #iterate whilst the number does not equal 1
        while num != 1:
            sum = 0
            #for each character (int) get the square value and add them together
            for x in str(num):
                sum += int(x) ** 2
            
            #set the next number to use as the sum of this  
            num = sum
            
            #this will ensure we dont fall into a circular loop 
            if num in used:
                break
            else:
                used.append(num) 
        
        #we could reach here by breaking out the loop or equalling 1, so check
        return num == 1
