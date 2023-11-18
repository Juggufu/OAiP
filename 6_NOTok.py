# Сортировка пузырьком
# def bubble_sort(array):
#     length = len(array)
#     for i in range(0, length):
#         for j in range(0, length - i - 1):
#             if array[j] > array[j + 1]:
#                 temp = array[j]
#                 array[j] = array[j + 1]
#                 array[j + 1] = temp
#
# arr = []
# n = int(input("кол-во елементов"))
# for i in range(0, n):
#     element = int(input('елемент[' + str(i + 1) + '] ='))
#     arr.append(element)
# bubble_sort(arr)
# print(arr)
# Сортировка вставками
# def insertion_sort(array):
#     length = len(array)
#     for i in range(1, length):
#         key = array[i]
#         j = i
#         while (j - 1 >= 0) and (array[j - 1] > key):
#             array[j - 1], array[j] = array[j], array[j - 1]
#             j = j - 1
#         array[j] = key
#
# arr = []
# length = int(input("кол-во елементов"))
# for i in range(0, length):
#     element = int(input("елемент [" + str(i + 1) + "] = "))
#     arr.append(element)
# insertion_sort(arr)
# print(arr)
# Сортировка слиянием
# def merge_sort(alist, start, end):
#     if end - start > 1:
#         mid = (start + end) // 2
#         merge_sort(alist, start, mid)
#         merge_sort(alist, mid, end)
#         merge_list(alist, start, mid, end)
#
#
# def merge_list(alist, start, mid, end):
#     left = alist[start:mid]
#     right = alist[mid:end]
#     k = start
#     i = 0
#     j = 0
#     while (start + i < mid and mid + j < end):
#         if (left[i] <= right[j]):
#             alist[k] = left[i]
#             i = i + 1
#         else:
#             alist[k] = right[j]
#             j = j + 1
#         k = k + 1
#     if start + i < mid:
#         while k < end:
#             alist[k] = left[i]
#             i = i + 1
#             k = k + 1
#     else:
#         while k < end:
#             alist[k] = right[j]
#             j = j + 1
#             k = k + 1
#
#
# alist = input('елементы').split()
# alist = [int(x) for x in alist]
# merge_sort(alist, 0, len(alist))
# print(alist)
# Быстрая сортировка
def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


alist = input('елементы: ').split()
alist = [int(x) for x in alist]
quicksort(alist, 0, len(alist))
print(alist)
