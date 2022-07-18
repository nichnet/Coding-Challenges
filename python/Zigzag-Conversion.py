#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
#    (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R

#And then read line by line: "PAHNAPLSIIGYIR"
#Write the code that will take a string and make this conversion given a number of rows.
    
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        arr = [[' '] * len(s) for y in range(numRows)]

        x = 0
        y = 0
        horiz = False

        for i in range(len(s)):
                arr[y][x] = s[i]

                if y == 0:
                    horiz = False
                elif y == numRows - 1:
                    horiz = True



                if horiz == True:
                    y -=1 
                    x += 1
                else:
                    y += 1


        out = ""    
        for x in range(len(arr)):
            for c in arr[x]:
                if not c == ' ':
                    out += str(c)

        return out
