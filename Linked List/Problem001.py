# Single Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def insertAtStart(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode

    def display(self):
        info = self.head
        while info:
            print(f"{info.data} -> ", end=" ")
            info = info.next
        print("None")

    def delete(self, element):
        if self.head is None:
            print("Linked List is Empty")
            return
        if self.head.data == element:
            self.head = self.head.next
            return
        temp = self.head
        prev = None
        while temp and temp.data != element:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next
            return
        print(f"{element} Not found !")

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
            self.head = newNode
            return
        temp = self.head
        current_index = 0
        while temp and current_index < index - 1:
            temp = temp.next
            current_index += 1
        if temp:
            newNode.next = temp.next
            temp.next = newNode
            return
        print("Index out of Range !")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(3)
obj.insertAtStart("Radha")
obj.delete(20)
obj.insertByIndex("Krishna", 1)
obj.update(3, 30)
obj.display()
