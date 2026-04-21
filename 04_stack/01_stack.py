

class stack:

    def __init__(self):
        self.s = []
    
    def length(self):
        return len(self.s)
    

    def push(self,val):
        self.s.insert(0,val)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("stack is empty")
        
        return self.s[0]
    
    def pop(self):
        if len(self.s) == 0 :
            raise Exception("stack is empty cannot delete")

        return self.s.pop(0)


stk = stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)

stk.pop(4)




