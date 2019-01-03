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