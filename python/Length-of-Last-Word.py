#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):

        words = []
        
        for x in s.split(' '):
            if x != '':
                words.append(x)
        
        #get the last word
        last = words[-1]
        
        return len(last)
