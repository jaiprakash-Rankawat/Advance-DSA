# double Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def insertAtStart(self, element):
        newNode = Node(element)
        # data = element, next = None , prev = None
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data} <-->", end=" ")
            temp = temp.next
        print("None")

    def Update(self, element, replace):
        temp = self.head
        if self.head is None:
            print("Linked List is Empty !")
        elif self.head is not None:
            while temp:  # temp is Not None
                if temp.data == element:
                    temp.data = replace
                    break
                temp = temp.next
            else:
                print(f"{element} Not found")

    def delete(self, element):
        # element = 30
        if self.head is None:
            print("linked list is empty")
            return

        if self.head.data == element:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head
        # 10 <--> 20 <--> 30 <--> 40 <--> None

        while temp and temp.data != element:
            temp = temp.next
            # temp.next.next =30 <--> 40 <--> None
        if temp:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            return
        print(f"{element} Not found")

    def insertByIndex(self, index, element):
        newNode = Node(element)
        if index == 0:

            # self.head = None
            if self.head is None:
                self.head = newNode
                return
            # None <- 10 -> 20 -> 30 -> None
            # newNode = data = "jd", next = 10 -> 20 -> 30 -> None , prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return
        current_index = 0
        temp = self.head
        # index = 2
        # self.head = 10 - > 20 -> 30 -> None
        while temp and current_index < index - 1:
            temp = temp.next
            # 20 -> 30 -> None
            current_index += 1
            # current_index = 1
        if temp:
            # newNode = data = radha , next = None , prev = None
            newNode.next = temp.next
            # radha -> 30 -> None
            temp.next.prev = newNode
            temp.prev.next = newNode
            newNode.prev = temp.prev
            self.head = newNode
            return
        print("Index not found")

    def info(self):
        print(self.head.next.prev.data)


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insertByIndex(2, "Radha")
obj.display()
obj.info()


# single linked list
# double linked list
# circuler linked list (single linked list)
# circuler linked list (double linked list)
