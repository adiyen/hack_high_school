def merge(train1, train2):
    node = train1
    while(node):
        if node.next == None:
            node.next = train2
            break

        else:
            node = node.next