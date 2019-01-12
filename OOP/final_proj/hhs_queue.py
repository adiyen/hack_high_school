class Queue:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next
        self.numbs = []
        
    def isEmpty(self):
        if self.numbs == []:
            return None
        return ""
        
    def enqueue(self, data):
        self.numbs.insert(0, data)
        
    def dequeue(self):
        self.numbs.pop()    
        
    def frontqueue(self):
        return self.numbs[-1]
    
    def size(self):
        return len(self.numbs)
    
    def __str__(self):
        return self.numbs

queue = Queue(0)
print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.frontqueue())
queue.dequeue()
print(queue.size())
print(queue.__str__())