class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

# List as collections
def printList(node):
    while node:
        print node,
        node = node.next
    print

# List and recursion
# 1. Separate the list into two piece: the first node(called the head);
# and the rest(called the tail).
# 2. Print the tail backward.
# 3. Print the head
def printBackward(list):
    if list == None: return
    head = list
    tail = list.next
    printBackward(tail)
    print head

if __name__ == "__main__":
    node = Node("test")
    print node
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    printList(node1)
    printBackward(node1)
