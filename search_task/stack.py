class Stack:

    #Constructor creates a list
    def __init__(self, data):
        self.stack = list()
        self.stack.append(data)
        
    #Adding elements to stack
    def push(self,data):
        self.stack.append(data)

    #Removing last element from the stack
    def pop(self):
        return self.stack.pop()
        
    #Getting the size of the stack
    def size(self):
        return len(self.stack)
    
    def elements(self):
        return self.stack
    
    