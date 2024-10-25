# Linked list


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
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def insertAtStart(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data} ->", end=" ")
            temp = temp.next
        print("None")

    # def Update(self, element, replace):
    #     if self.head is None:
    #         print("Linked List is Empty !")
    #         return
    #     temp = self.head
    #     while temp:  # temp is Not None
    #         if temp.data == element:
    #             temp.data = replace
    #             return
    #         temp = temp.next
    #     print(f"{element} Not found")
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
        if self.head is None:
            print("linked list is empty")
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
        print(f"{element} Not found")

    def insertByIndex(self, index, element):
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
        print("Out of index")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insert(40)
obj.display()


# single linked list
# double linked list
# circuler linked list (single linked list)
# circuler linked list (double linked list)
