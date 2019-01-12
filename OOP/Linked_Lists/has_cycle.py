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

def has_cycle(list_head):
    node = list_head
    node = node.next
    while(node):
        if node.next == None:
            return "False"
        if node == list_head:
            return "True"
            node = node.next
        else:
            node = node.next  

n1 = Node(30)
n2 = Node(20)
n3 = Node(10)
n4 = Node(60)
n5 = Node(50)
n6 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

print(has_cycle(n1))