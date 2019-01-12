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

def remove_lightest(head_node, list_length):
    prev_node = head_node
    node = prev_node.next
    counter = 1
    while(node):
        if counter >= list_length-2:
            prev_node.next = None
        
        prev_node = node
        node = node.next
        counter+=1
    
    return head_node

def length(list):
    node = list
    list_length = 0
    while(node):
        node = node.next
        list_length+=1
    return list_length

def sort_desc(unsorted_list):
    list_length = length(unsorted_list)

    min_node = unsorted_list
    min_finder = min_node.next
    
    count = min_finder
    
    while(min_finder):
        if min_finder.content > min_node.content:
            prev_min_node = count
            min_node = min_finder
       
        count = min_finder   
        min_finder = min_finder.next
    
    if min_node.content != unsorted_list.content:
        storage = unsorted_list.next
        unsorted_list.next = min_node.next
        min_node.next = storage
        prev_min_node.next = unsorted_list

    head_node = min_node
    for i in range(list_length):
        prev_prev_node = head_node
        prev_node = prev_prev_node.next
        node = prev_node.next
        while node:
            if prev_node.content < node.content:
                prev_node.next, node.next, prev_prev_node.next = node.next, prev_node, node
                prev_node, node = node, prev_node       
            else:
                prev_prev_node, prev_node, node = prev_node, node, node.next
    
    print(remove_lightest(head_node, list_length))

def merge(train1, train2):
    node = train1
    while(node):
        if node.next == None:
            node.next = train2
            break

        else:
            node = node.next
            
    sort_desc(train1)


n1 = Node(30)
n2 = Node(20)
n3 = Node(10)
n4 = Node(60)
n5 = Node(50)
n6 = Node(40)

n1.next = n2
n2.next = n3
n4.next = n5
n5.next = n6

merge(n1, n4)