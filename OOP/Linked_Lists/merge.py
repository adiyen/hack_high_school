class Node:
  def __init__(self, content):
    self.c = content
    self.n = None
    
  @property
  def content(self):
    return self.c
  
  @property
  def next(self):
    return self.n
  
  @next.setter
  def next(self, node):
    self.n = node
    
  @content.setter
  def content(self, val):
    self.c = val
    
  def __repr__(self):
    return f"Node Value: {self.c}"

def merge(train1, train2):
    node = train1
    while(node):
        if node.next == None:
            node.next = train2
            break

        else:
            node = node.next
    return train1

n1 = Node(60)
n2 = Node(50)
n3 = Node(40)
n4 = Node(30)
n5 = Node(20)
n6 = Node(10)

n1.next = n2
n2.next = n3
n4.next = n5

print(merge(n1, n4))