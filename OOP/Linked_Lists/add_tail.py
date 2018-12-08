def add_tail(list_head, val):
    node = list_head
    while(node):
        if node.next is None:
            new_node = Node(val)
            node.next = new_node
            break
        else:
            node = node.next