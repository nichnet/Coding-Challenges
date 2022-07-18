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
