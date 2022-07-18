#There is a special keyboard with all keys in a single row.
#Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.
#You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

class Solution(object):
    def calculateTime(self, keyboard, word):
        
        moves = 0

        curr = 0
        for i in word:
            nextt = keyboard.index(i)
            
            
            val = curr - nextt
                
            #abs value
            if val < 0:
                val = -val
            
            moves += val
            
            curr = nextt
        
        return moves
