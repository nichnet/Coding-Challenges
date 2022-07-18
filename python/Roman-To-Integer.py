class Solution(object):
    keys = {
        'M': 1000, 
        'D': 500,        
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    
    def romanToInt(self, s):
        out = 0
        lastChar = None

        for i in range(len(s), 0, -1):
            c = s[i - 1] #char
            value = self.keys[c] #numerical value

            if (c == 'I' and (lastChar == 'V' or lastChar == 'X')) or (c == 'X' and (lastChar == 'L' or lastChar == 'C')) or (c == 'C' and (lastChar == 'D' or lastChar == 'M')):
                out -= value
            else:
                out += value

            lastChar = c

        return out
        
