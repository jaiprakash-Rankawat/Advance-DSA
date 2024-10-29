# circuler Linked list (single linked List)


# important thing (ctrl + alt + M)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):
        newNode = Node(element)
        # case 1: linked list is empty
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        # case 2: linked list not empty
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head

    def insertAtStart(self, element):
        newNode = Node(element)
        newNode.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        self.head = newNode

    def display(self):
        # case 1 : Linked list is empty

        if self.head is None:
            print("Linked list is empty")
            return

        # case 2: circuler linked list

        temp = self.head
        while True:
            print(f"{temp.data} -> ", end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("Head")

    def update(self, element, replace):
        # case 1: linked list is empty
        if self.head is None:
            print("can not update : Linked List is Empty")
            return

        # case 2 : if element exist
        temp = self.head
        while True:
            if temp.data == element:
                temp.data = replace
                return
            temp = temp.next
            if temp == self.head:
                break

        # case 3 : element is not exit
        print(f"{element} Not found")

    def delete(self, element):
        # case 1 : linked list is empty
        if self.head is None:
            print("linked list is empty")
            return

        # case 2 : linked list is not empty
        temp = self.head
        while True:
            temp = temp.next
            if temp.data == element:
                temp = temp.next
                return
            if temp == self.head:
                break
        # case 3 : element not found
        print(f"{element} Not found")

    # def info(self):
    #     print(self.head.next.next.next.next.next.data)


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.delete(30)
obj.display()
# obj.info()
