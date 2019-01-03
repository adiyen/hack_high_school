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

def length(list):
    node = list
    list_length = 0
    while(node):
        node = node.next
        list_length+=1
    return list_length

def sort_asc(unsorted_list):
    list_length = length(unsorted_list)

    min_node = unsorted_list
    min_finder = min_node.next
    
    count = min_finder
    
    while(min_finder):
        if min_finder.content < min_node.content:
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
            if prev_node.content > node.content:
                prev_node.next, node.next, prev_prev_node.next = node.next, prev_node, node
                prev_node, node = node, prev_node       
            else:
                prev_prev_node, prev_node, node = prev_node, node, node.next
                  
    # print_node = head_node
    # while print_node:
    #     print(print_node)
    #     print_node = print_node.next

n1 = Node(-2)
n2 = Node(-3)
n3 = Node(25)
n4 = Node(20)
n5 = Node(80)
n6 = Node(12)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
sort_asc(n1)