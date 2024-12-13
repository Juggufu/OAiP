import cProfile
import random


def bubble_sort(numbers):
    swap = True
    for i in range(len(numbers) - 1):
        if swap == False:
            break
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swap = True
            else:
                swap = False
    return numbers

def bubble_sort(numbers):
    n = len(numbers)
    swap = True
    start = 0
    end = n - 1
    while swap:
        swap = False
        for j in range(start, end):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swap = True
        if not swap:
            break
        swap = False
        end -= 1
        for j in range(end-1, start-1, -1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swap = True
        start += 1
    return numbers


array_size = 1000
numbers = [random.randint(1, 100) for _ in range(array_size)]
cProfile.run('bubble_sort(numbers)')