#Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#A shift on s consists of moving the leftmost character of s to the rightmost position.
# -  For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution(object):
    def rotateString(self, s, goal):
        
        
        val = s
        
        for i in range(len(s)):
            l = val[0] 
            r = val[1::]
            
            val = r + l
            
            if val == goal:
                return True
            
        
        return False
        
