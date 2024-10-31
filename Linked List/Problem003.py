# circuler linked list


# 10 -> 20 -> 30-> head
# ctrl + alt + M = to stop the infinite loop
# while True:
#     print("jai")


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

        # case 2: linked list is not empty
        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = newNode
        newNode.next = self.head

    def insertAtStart(self, element):
        newNode = Node(element)

        # case 1: linked list is empty
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return

        # case 2: linked list is not Empty

        # "nilesh" -> 10 -> 20 -> 30-> head

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        newNode.next = self.head
        temp.next = newNode
        self.head = newNode

    def display(self):

        # case 1 : linked list is empty
        if self.head is None:
            print("linked list is empty")
            return

        # case 2 : linked list is not empty

        temp = self.head
        while True:
            print(f"{temp.data} ->", end=" ")
            temp = temp.next

            if temp == self.head:
                break
        print("Head")

    def info(self):
        print(self.head.next.next.next.next.data)

    def delete(self, element):

        # case 1 : linked list is empty

        if self.head is None:
            print("linked list is empty")
            return

        # case 2: element at first position

        if self.head.data == element:

            # case 3 : linked list have only one element
            # 10 -> head
            # self.head = None

            if self.head == self.head.next:
                self.head = None
                return

            # case 4 : linked list have multiple element

            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            # 10 -> 20 -> 30-> head
            self.head = self.head.next
            # 20 -> 30-> head
            temp.next = self.head
            return
            # 20 -> 30-> head

        # case 5: element is present at Nth positon

        temp = self.head
        while temp.next != self.head:
            if temp.next.data == element:
                temp.next = temp.next.next
                return
            temp = temp.next
        # case 6: element not found
        print(f"{element} Not found")

    def update(self, element, replace):

        # case 1 : linked list is empty
        if self.head is None:
            print("Linked list is empty")
            return

        # case 2 : element present at nth position
        temp = self.head
        while True:
            if temp.data == element:
                temp.data = replace
                return
            temp = temp.next
            if temp == self.head:
                break
        print(f"{element} Not found")

    def insertAtIndex(self, index, element):
        newNode = Node(element)
        # case 1 : if index is 0

        if index == 0:
            # case 2 : linked list is empty

            if self.head is None:
                self.head = newNode
                newNode.next = self.head
                return

            # case 3 : linked list is not empty
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newNode.next = self.head
            temp.next = newNode
            self.head = newNode
            return

        # case 4: if index != 0

        current_index = 0
        temp = self.head

        while temp.next != self.head and current_index < index - 1:
            temp = temp.next
            current_index += 1

        # case 5 : value to be inserted
        if current_index == index - 1:
            newNode.next = temp.next
            temp.next = newNode
            return
        # case 6 : out of index
        print("out of index")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insertAtStart("Radha")
obj.insertAtIndex(0, "Nilesh")
obj.insertAtIndex(2, "jp")
obj.insertAtIndex(10, "alsdkjfo;a")


obj.display()


# Home Work

# single circuler linked list
# 10 -> 20 -> 30 -> head

# double circuler linked list
# 10 -> 20 -> 30 -> head
# 10 <- 20 <- 30 <- head
