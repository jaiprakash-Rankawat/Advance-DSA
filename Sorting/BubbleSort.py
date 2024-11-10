# array = [20,5,12,45,6,11]
# array = [5,20,12,45,6,11]
# array = [5,12,20,45,6,11]
# array = [5,12,20,45,6,11]
# array = [5,12,20,6,45,11]
# array = [5,12,20,6,11,45]
# array = [5,12,6,20,11,45]
# array = [5,12,6,11,20,45]
# array = [5,6,12,11,20,45]
# array = [5,6,11,12,20,45]


# bubble sort


def BubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array = [20, 5, 16, 4, 15, 8]
jd = BubbleSort(array)
print("sorted Array : ", BubbleSort(array))
