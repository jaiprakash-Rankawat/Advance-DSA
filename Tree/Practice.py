# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert(self, element):
#         newNode = Node(element)

#         # case1: tree is empty
#         if self.root is None:
#             self.root = newNode
#             return

#         # case 2: tree is Not empty
#         self.insertAgain(self.root, element)

#     def insertAgain(self, current, data):
#         if current.data < data:
#             if current.right is None:
#                 current.right = Node(data)
#             else:
#                 self.insertAgain(current.right, data)
#         elif current.data > data:
#             if current.left is None:
#                 current.left = Node(data)
#             else:
#                 self.insertAgain(current.left, data)

#     def serach(self, element):
#         # case 1: tree is empty
#         if self.root is None:
#             print("Tree is empty")
#             return
#         self.serachElement(self.root, element)

#     def searchElement(self, current, data):
#         if current is None:
#             print(f"{data} Not found")
#         elif current.data == data:
#             print(f"{data} found")
#         else:
#             if current.data < data:
#                 self.searchElement(current.right, data)
#             else:
#                 self.searchElement(current.left, data)

#     def inorder(self):
#         print("Inorder :", end=" ")
#         self.Inorder(self.root)
#         print()

#     def Inorder(self, current):
#         if current:
#             self.Inorder(current.left)
#             print(current.data, end=" ")
#             self.Inorder(current.right)

#     def postorder(self):
#         print("PostOrder :", end=" ")
#         self.Postorder(self.root)
#         print()

#     def Postorder(self, current):
#         if current:
#             self.Postorder(current.left)
#             self.Postorder(current.right)
#             print(current.data, end=" ")

#     def preorder(self):
#         print("preorder : ", end=" ")
#         self.Preorder(self.root)
#         print()

#     def Preorder(self, current):
#         if current:
#             print(current.data, end=" ")
#             self.Preorder(current.left)
#             self.Preorder(current.right)

#     def delete(self, element):

#         self.deleteElement(self.root, element)

#     def deleteElement(self, current, data):
#         if current is None:
#             return current
#         if data < current.data:
#             current.left = self.deleteElement(current.left, data)
#         elif data > current.data:
#             current.right = self.deleteElement(current.right, data)
#         else:
#             if current.left is None:
#                 return current.right
#             elif current.right is None:
#                 return current.left

#             temp = self.min(current.right)
#             current.data = temp.data
#             self.deleteElement(current.right, temp.data)
#         return current

#     def min(self, current):
#         while current:
#             current = current.left
#         return current

#     def levelorder(self):
#         print("Level Order :", end=" ")
#         queue = [self.root]
#         while queue:
#             current = queue[0]
#             print(current.data, end=" ")

#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)
#             queue.pop(0)


# obj = Tree()
# obj.insert(7)
# obj.insert(5)
# obj.insert(15)
# obj.insert(1)
# obj.insert(10)
# obj.insert(3)
# obj.inorder()
# obj.postorder()
# obj.preorder()

# obj.delete(1)
# obj.inorder()
# obj.levelorder()


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        newNode = Node(element)
        if self.root is None:
            self.root = newNode

            return
        self.Insert_element(self.root, element)

    def Insert_element(self, current, data):
        if current.data < data:
            if current.right is None:
                current.right = Node(data)
            else:
                self.Insert_element(current.right, data)
        else:
            if current.left is None:
                current.left = Node(data)
            else:
                self.Insert_element(current.left, data)

    def search(self, element):
        if self.root is None:
            print("Tree is empty")
            return
        self.search_element(self.root, element)

    def search_element(self, current, data):
        if current is None:
            print(f"{data} not found")
        elif current.data == data:
            print(f"{data} found")
        else:
            if current.data > data:
                self.search_element(current.left, data)
            else:
                self.search_element(current.right, data)


obj = Tree()
obj.insert(10)
obj.insert(7)
obj.insert(12)
obj.insert(11)
obj.search(12)
