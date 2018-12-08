def remove(list_head, val):
    node = list_head
    prev_node = None
    while(node):
        if node.content == val and list_head.content != val:
            prev_node.next = node.next
            break
        prev_node = node
        node = node.next