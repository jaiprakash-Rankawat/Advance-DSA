# linear search


# array = [10,20,30,40,50,60,70]
# target = 50 ( 50 found , 50 not found)


# def LinearSearch(array, target):
#     for i in array:
#         if i == target:
#             print(f"{target} found")
#             return
#     print(f"{target} not found ")


# array = [25, 15, 6, 4, 92, 45, 26]
# target = 50
# LinearSearch(array, target=25)


# binary search

# 1.data must be in ascending order


# array = [10,20,30,40,50,60,70]
# left = 0
# right = 7-1
# mid = (left + right)//2 #3


def BinarySearch(array, target):

    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            print(f"{target} found")
            return
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(f"{target} not found")


array = [10, 20, 30, 40, 50, 60, 70, 80]
target = 30
BinarySearch(array, target=15)
