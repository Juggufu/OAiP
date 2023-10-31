def main():
    n = int(input())
    numbers = []
    s = 0
    for i in range(n + 1):
        numbers.append(i)
    numbers[1] = 0
    i = 2
    while i <= n:
        if numbers[i] != 0:
            j = 2 * i
            while j <= n:
                numbers[j] = 0
                j += i
        i += 1
    numbers = set(numbers)
    numbers.remove(0)
    print(sum(numbers))

if __name__ == "__main__":
    main()