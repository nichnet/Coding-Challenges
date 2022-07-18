#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack

class Solution(object):
    def strStr(self, haystack, needle):
        needle_len = len(needle) #length of the needle

        for i in range (len(haystack)): #iterate each character in haystack
            
            xx = 0
            matched = 0 #number of matched chars
            
            subrange = i + needle_len #length of i index + length of needle 

            if subrange > len(haystack):
                break #break if out of bounds

            for j in range(i, subrange, 1): #iterate sub string
                if haystack[j] == needle[xx]: #if matched , add
                    matched += 1

                xx += 1 #iterate to next needle char
        
            if matched == len(needle):
                return i #return the index if the matched chars is correct
    
        return -1
