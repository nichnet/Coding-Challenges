#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.
# -  For example, 121 is a palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        xx = str(x)
        len_ = len(xx) - 1
        
        for i in range(len_):
            forward = xx[i]
            backward = xx[len_ - i]
            
            if not forward == backward:
                return False
        
        return True
