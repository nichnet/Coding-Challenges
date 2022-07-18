class Solution(object):
    def lengthOfLastWord(self, s):

        words = []
        
        for x in s.split(' '):
            if x != '':
                words.append(x)
        
        #get the last word
        last = words[-1]
        
        return len(last)
