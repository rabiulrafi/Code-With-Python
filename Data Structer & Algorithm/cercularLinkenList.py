class Node():
    def __init__(self, item=None, next_node =None):
        self.item = item
        self.next_node = next_node

class CircularLinkedList():
    def __init__(self, head = Node):
        self.head = head

    def appendleft(self, item):
        new_node = Node(item)
        new_node.next_node = self.head
        current = self.head
        if self.head is not None:
            while current.next_node is not self.head:
                current = current.next_node

            current.next_node = new_node
        else:
            new_node.next_node =  new_node
        self.head = new_node

    