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
