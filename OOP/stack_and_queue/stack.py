class stack:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next
        self.numbs = []
    
    def isEmpty(self):
        if self.numbs == []:
            return None
        
    def push(self, data):
        self.numbs.append(data)
    
    def pop(self):
        self.numbs.pop()

    def peek(self):
        return self.numbs[-1]
    
    def size(self):
        return len(self.numbs)
    
    def __str__(self):
        print(self.numbs)

stack = stack(0)
print(stack.isEmpty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
print(stack.peek())
print(stack.size())
stack.__str__()