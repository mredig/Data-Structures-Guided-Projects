class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


def printLL(startNode):
    currentNode = startNode
    while currentNode is not None:
        print(currentNode.value)
        currentNode = currentNode.next


"""Find middle of single linked list 1 iteration"""
def findLLMid2(singleLinkList):
    currentNode = singleLinkList
    middleNode = currentNode
    try:
        currentNode = currentNode.next.next
    except:
        currentNode = None
    while currentNode is not None:
        middleNode = middleNode.next
        try:
            currentNode = currentNode.next.next
        except:
            currentNode = None
    return middleNode.value


print("Finding middle")

bListA = Node(1)
bListB = Node(2)
bListC = Node(3)
bListD = Node(4)
bListE = Node(5)

bListA.next = bListB
bListB.next = bListC
bListC.next = bListD

print(findLLMid2(bListA))  # 2

bListD.next = bListE
print(findLLMid2(bListA))  # 3


"""reverse single linked list, 1 iteration, no recursion"""
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


print("")
print("reversing list")

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

print("before")
printLL(a)

reverseSLL(a)

print("after")
printLL(e)
