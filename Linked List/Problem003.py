# single linked list


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, element):
#         newNode = Node(element)
#         if self.head is None:
#             self.head = newNode
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = newNode

#     def insertAtStart(self, element):
#         newNode = Node(element)
#         newNode.next = self.head
#         self.head = newNode

#     def delete(self, element):
#         if self.head is None:
#             print("Linked List is Empty")
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
#             print(f"{element} Not found ")

#     def display(self):
#         info = self.head
#         while info:
#             print(f"{info.data} -> ", end=" ")
#             info = info.next
#         print("None")

#     def insertAtIndex(self, element, index):
#         newNode = Node(element)
#         if index == 0:
#             newNode.next = self.head
#             self.head = newNode
#             return
#         info = self.head
#         current_index = 0
#         while info and current_index < index - 1:
#             info = info.next
#             current_index += 1
#         if info:
#             newNode.next = info.next
#             info.next = newNode
#         else:
#             print("Index out of Range")

#     def update(self, element, replace):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         if self.head.data == element:
#             self.head.data = replace
#             return
#         info = self.head
#         while info:
#             if info.data == element:
#                 info.data = replace
#                 return
#             info = info.next
#         print(f"{element} Not found")


# obj = LinkedList()
# obj.insert(10)
# obj.insert(20)
# obj.insert(30)
# obj.insertAtStart("Radha")
# obj.delete(10)
# obj.delete(30)
# obj.insertAtIndex("jp", 0)
# obj.insertAtIndex("jp", 1)
# obj.insertAtIndex("jp", 5)
# obj.display()


# Double linked list


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, element):
#         newNode = Node(element)
#         if self.head is None:
#             self.head = newNode
#             newNode.prev = self.head
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = newNode
#         newNode.prev = last

#     def insertAtStart(self, element):
#         newNode = Node(element)
#         if self.head is None:
#             self.head = newNode
#             return
#         newNode.next = self.head
#         self.head.prev = newNode
#         self.head = newNode

#     def display(self):
#         info = self.head
#         while info:
#             print(f"{info.data} <--> ", end=" ")
#             info = info.next
#         print("None")

#     def delete(self, element):
#         if self.head is None:
#             print("Linked List is Empty")
#             return
#         if self.head.data == element:
#             self.head = self.head.next
#             self.head.prev = None
#             return
#         last = self.head
#         while last and last.data != element:
#             last = last.next
#         if last:
#             if last.next:
#                 last.next.prev = last.prev
#             if last.prev:
#                 last.prev.next = last.next
#             return
#         print(f"{element} Not found")

#     def update(self, element, replace):
#         if self.head is None:
#             print("Linked List is Empty")
#             return
#         if self.head.data == element:
#             self.head.data = replace
#             return
#         info = self.head
#         while info:
#             if info.data == element:
#                 info.data = replace
#                 return
#             info = info.next
#         print(f"{element} not found")

#     def insertAtIndex(self, index, element):
#         newNode = Node(element)
#         if index == 0:
#             if self.head is None:
#                 self.head = newNode
#                 return
#             newNode.next = self.head
#             self.head.prev = newNode
#             self.head = newNode
#             return
#         temp = self.head
#         current_index = 0
#         while temp and current_index < index - 1:
#             temp = temp.next
#             current_index += 1

#         if temp:
#             newNode.next = temp.next
#             if temp.next:
#                 temp.next.prev = newNode
#             temp.next = newNode
#             newNode.prev = temp
#             return
#         print("Index Out of range ")


# obj = LinkedList()
# obj.insert(10)
# obj.insert(20)
# obj.insert(30)
# obj.insertAtStart("Radha")
# obj.delete(20)
# obj.insertAtIndex(0, "krishna")
# obj.insertAtIndex(4, "krishna")
# obj.display()


# # Single circuler Linked list


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, element):
#         newNode = Node(element)
#         if self.head is None:
#             self.head = newNode
#             newNode.next = self.head
#             return
#         temp = self.head
#         while temp.next != self.head:
#             temp = temp.next
#         temp.next = newNode
#         newNode.next = self.head

#     def insertAtStart(self, element):
#         newNode = Node(element)
#         temp = self.head
#         while temp.next != self.head:
#             temp = temp.next
#         newNode.next = self.head
#         self.head = newNode
#         temp.next = self.head

#     def display(self):
#         info = self.head
#         while True:
#             print(f"{info.data} -> ", end=" ")
#             info = info.next
#             if info == self.head:
#                 break

#     def delete(self, element):
#         # concept 1
#         # 10 -> 20 -> 30
#         if self.head is None:
#             print("Linked List is Empty")
#             return
#         temp = self.head
#         if temp.data == element:
#             temp = temp.next
#             if temp:
#                 while temp.next != self.head:
#                     temp = temp.next
#                 temp.next = self.head
#                 return

#     def info(self):
#         print(self.head.next.next.next.data)


# obj = LinkedList()
# obj.insert("Radha")
# obj.insert("Krishan")
# obj.insertAtStart("ram")
# obj.info()
# obj.delete("ram")
# obj.display()


# Double linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,element):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def insertAtStart(self,element):
        newNode = Node(element)
        newNode.next = self.head
        self.head.prev = None
        self.head = newNode
    def 
