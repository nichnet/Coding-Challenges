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
