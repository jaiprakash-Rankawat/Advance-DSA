# # single linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self,element):
#         newNode = Node(element)
#         if self.head is None:
#             self.head = newNode
#             return

#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = newNode
#     def insertAtStart(self,element):
#         newNode = Node(element)
#         newNode.next = self.head
#         self.head = newNode

#     def display(self):
#         temp = self.head

#         while temp:
#             print(f"{temp.data} ->",end=" ")
#             temp = temp.next
#         print("None")

#     def delete(self,element):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         if self.head.data == element:
#             self.head = self.head.next
#             return
#         temp = self.head
#         prev = None
#         while temp and temp.data != element:
#             prev = temp
#             temp = temp.next

#         if temp:
#             prev.next = temp.next
#         else:
#             print(f"{element} Not found")

#     def insertAtIndex(self,element,index):
#         newNode = Node(element)
#         if index==0:
#             newNode.next = self.head
#             self.head = newNode
#             return

#         temp = self.head
#         current_index = 0
#         while temp and current_index < index -1:
#             temp = temp.next
#             current_index +=1

#         if temp:
#             newNode.next = temp.next
#             temp.next = newNode
#             return
#         print("Index out of Range")

#     def update(self,element,replace):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         if self.head.data == element:
#             self.head.data = replace
#             return
#         temp = self.head
#         while temp:
#             if temp.data == element:
#                 temp.data = replace
#                 return
#             temp = temp.next
#         print(f"{element} Not found")


# double Linked list
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
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data} <-->", end=" ")
            temp = temp.next
        print("None")

    def delete(self, element):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == element:
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
                return
            self.head = None
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

    def update(self, element, update):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == element:
            self.head.data = update
            return
        temp = self.head
        while temp:
            if temp.data == element:
                temp.data = update
                return
            temp = temp.next
        print(f"{element} not found")

    def insertByIndex(self, element, index):
        newNode = Node(element)
        if index == 0:
            if self.head is None:
                self.head = newNode
                return
            newNode.next = self.head
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
            if temp.next:
                temp.next.prev = newNode
            temp.next = newNode
            newNode.prev = temp
            return
        print("Index out of range")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.insertAtStart("Radha")
obj.insertByIndex("krishna", 3)
obj.display()
