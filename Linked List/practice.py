# circuler linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, elemnet):
        newNode = Node(elemnet)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head

    def insertAtStart(self, element):
        newNode = Node(element)
        newNode.next = self.head
        temp = self.head
        while True:
            if temp.next == self.head:
                break
            temp = temp.next
        temp.next = newNode
        self.head = newNode

    def display(self):
        if self.head is None:
            print("linked list is empty")
            return
        temp = self.head
        while True:
            print(f"{temp.data} -> ", end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print("Head")

    def delete(self, element):
        if self.head is None:
            print("linked list is empty")
            return
        temp = self.head
        if self.head.data == element:
            while True:
                if temp.next == self.head:
                    break
                temp = temp.next
            if self.head == self.head.next:
                self.head = None
                return
            self.head = self.head.next
            temp.next = self.head
            return
        while temp.next != self.head:
            if temp.next.data == element:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"{element} Not found")

    def update(self, element, replace):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.head
        while temp.next != self.head:
            if temp.data == element:
                temp.data = replace
                return
            temp = temp.next
            if temp == self.head:
                return
        print(f"{element} Not found")

    def insertByIndex(self, index, element):
        newNode = Node(element)
        temp = self.head
        if index == 0:
            if self.head is None:
                self.head = newNode
                return
            newNode.next = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            self.head = newNode
            return
        current_index = 0
        while temp.next != self.head and current_index < index - 1:
            temp = temp.next
            current_index += 1

        if current_index == index - 1:
            newNode.next = temp.next
            temp.next = newNode
            return
        print("out of index")

    def info(self):
        print(self.head.next.data)


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insertAtStart("Radha")
obj.delete("Radha")
obj.update(20, "Ram")
obj.insertByIndex(0, "Radha")
obj.display()
