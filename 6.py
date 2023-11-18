# # Сортировка пузырьком
# arr = []
# n = int(input("кол-во елементов: "))
# for i in range(0, n):
#     element = int(input('Введите елемент: '))
#     arr.append(element)
# for run in range(n-1):
#     for i in range(n - 1):
#         if arr[i]>arr[i+1]:
#             arr[i],arr[i + 1] = arr[i+1],arr[i]
# print(*arr)
# Сортировка вставками
# arr = []
# n = int(input("кол-во елементов: "))
# for i in range(0, n):
#     element = int(input('Введите елемент: '))
#     arr.append(element)
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if arr[j]< arr[j-1]:
#             arr[j],arr[j - 1] = arr[j - 1],arr[j]
#         else:
#             break
# print(arr)
