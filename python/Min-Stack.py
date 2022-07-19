class MinStack(object):

    def __init__(self):
        self.stack = []


    def push(self, val):
        #if stack is length 0, then just add and return 
        if len(self.stack) == 0: 
            
            self.stack.append((val, val)) # (value , min value)
            return
            
        #get the next min value
        min = val

        if self.stack[0][1] < val:
            min = self.stack[0][1]
        
        #create temp array and fill it with the stack data
        temp = []

        temp.append((val, min))
        
        #extend existing 
        temp.extend(self.stack)

        self.stack = temp
        

    def pop(self):
        #set stack as (2nd el) 1st to end 
        self.stack = self.stack[1:]

    def top(self):
        #return the top value
        return self.stack[0][0]
        

    def getMin(self):
        #the top value will contain the min value as second property
        return self.stack[0][1]
