#Given a string s, return the number of segments in the string.
#A segment is defined to be a contiguous sequence of non-space characters.

class Solution(object):
    def countSegments(self, s):
        arr = []
        
        for i in s.split(' '):
            if not i == '':
                arr.append(i)
            
        print(arr)
            
        return len(arr)
