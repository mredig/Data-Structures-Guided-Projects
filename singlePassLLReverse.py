class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


def reverseSLL(startNode):
    currentNode = startNode

    currentFront = None
    while currentNode is not None:
        nextNode = currentNode.next
        if currentFront is None:
            currentFront = currentNode
            currentFront.next = None
        else:
            currentNode.next = currentFront
            currentFront = currentNode
        currentNode = nextNode


def printLL(startNode):
    currentNode = startNode
    while currentNode is not None:
        print(currentNode.value)
        currentNode = currentNode.next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

printLL(a)

reverseSLL(a)

print("a")
printLL(a)

print("e")
printLL(e)
