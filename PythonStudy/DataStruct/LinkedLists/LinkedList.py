class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

    def printBackward(self):
        if self.next != None: 
            tail = self.next
            tail.printBackward()
        print self.cargo

    def printList(self):
        nextNode = self
        while nextNode != None:
            print nextNode.cargo
            nextNode = nextNode.next

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def printBackward(self):
        print "[",
        if self.head != None:
            self.head.printBackward()
        print "]"

    def printList(self):
        print "[",
        if self.head != None:
            self.head.printList()
        print "]"

    def addFirst(self,cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.addFirst(1)
    linkedList.addFirst(2)
    linkedList.addFirst(3)
    linkedList.printList()
    linkedList.printBackward()
    print linkedList.length

