# Single Linked List


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
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode
        newNode.prev = last

    def insertAtStart(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def display(self):
        info = self.head
        while info:
            print(f"{info.data} <--> ", end=" ")
            info = info.next
        print("None")

    def delete(self, element):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == element:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        while temp and temp.data != element:
            temp = temp.next
        if temp:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            return
        print(f"{element} Not found")

    def update(self, element, replace):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data == element:
            self.head.data = replace
            return
        info = self.head
        while info:
            if info.data == element:
                info.data = replace
                return
            info = info.next
        print(f"{element} Not Found")

    def insertByIndex(self, element, index):
        newNode = Node(element)
        if index == 0:
            newNode.next = self.head
            if self.head:
                self.head.prev = newNode
            self.head = newNode
            return
        temp = self.head
        current_index = 0
        while temp and current_index < index - 1:
            temp = temp.next
            current_index += 1
        if temp:
            newNode.next = temp.next
            newNode.prev = temp
            if temp.next:
                temp.next.prev = newNode
            temp.next = newNode

            return
        print("Index out of Range !")

    def info(self):
        print(self.head.next.next.data)
        print(self.head.next.next.next.prev.data)


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.insertByIndex("Radha", 2)
obj.display()
obj.info()
