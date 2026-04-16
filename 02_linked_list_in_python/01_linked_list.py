class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self,head=None):
        self.head = head

    
    def insertAtEnd(self,data):
        if self.head == None:
            self.head = Node(data)
            return
        
        mover = self.head
        while(mover.next != None):
            mover=mover.next
        new_node = Node(data)
        mover.next = new_node

    def printLL(self):
        mover = self.head

        while(mover != None):
            print(mover.data ,end=" ")
            mover = mover.next
        print()


    def insertAtBeg(self,data):
        new_node = Node(data)        
        new_node.next = self.head
        self.head = new_node


    def insertInMiddle(self,data,x):
        mover = self.head
        new_node = Node(data)
        while(mover.next != None):
            if mover.data == x:
                new_node.next = mover.next
                mover.next = new_node
            mover = mover.next

    def deleteLL(self, data):
        if self.head is None:
            return

        # Case 1: deleting head
        if self.head.data == data:
            self.head = self.head.next
            return

        # Case 2: deleting non-head node
        mover = self.head
        prev = None

        while mover is not None:
            if mover.data == data:
                prev.next = mover.next
                return
            prev = mover
            mover = mover.next
            


ll = SinglyLinkedList()

ll.insertAtEnd(5)
ll.insertAtEnd(34)
ll.insertAtEnd(25)

ll.insertAtBeg(10)

ll.insertInMiddle(99,34)

ll.deleteLL(25)

ll.printLL()



