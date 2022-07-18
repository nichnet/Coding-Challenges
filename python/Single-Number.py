class Solution(object):
    def singleNumber(self, nums):
        
        doubles = []
        
        #iterate each number
        for i in nums:
            #if the number does not exist in the doubles array, 
            if i not in doubles:
                #then add it
                doubles.append(i)
            else:
                #if it does exist in the doubles array, then remove the existing one
                doubles.remove(i)
        #return the first instance..
        return doubles[0]
