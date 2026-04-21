

class Node :
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next =  None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            return

        mover = self.head
        while mover.next != None:
            mover=mover.next

        mover.next = new_node
        new_node.prev = mover


    def printDLL(self):
        mover = self.head

        while mover :
            print(mover.data ,end = " ")
            mover= mover.next

        print()        

    def insertAtBeg(self,data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insertAtMiddle(self,val,x):

        if self.head == None:
            return
        new_node = Node(x)
        
        mover = self.head
        while(mover.next !=None):
            if (mover.data == val):
                break
            else :
                mover = mover.next
                
        new_node.next = mover.next
        mover.next.prev = new_node
        mover.next = new_node 

    
    def deletionDLL(self,value):
        if self.head == None:
            print("Linked List is empty")
            return 

        mover = self.head

        if (mover.data == value):
            self.head = mover.next
            self.head.prev = None
            return

        while(mover.next):
            if (mover.data == value):
                mover.prev.next = mover.next
                mover.next.prev = mover.prev
                return
            else:
                mover = mover.next
        if (mover.data == value):
            mover.prev.next = None


        





dll = DoublyLinkedList()
dll.insertAtEnd(30)
dll.insertAtEnd(0)

dll.insertAtMiddle(30,14)

dll.insertAtBeg(3)

dll.deletionDLL(30)

dll.insertAtBeg(5)

dll.insertAtMiddle(5,1)


dll.deletionDLL(5)
dll.insertAtEnd(40)

dll.deletionDLL(40)
dll.printDLL()



             