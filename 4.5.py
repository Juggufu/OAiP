def main():
    a = int(input())
    s = 0
    for i in range(1, a + 1):
        if a % i == 0:
            s += i
    print(s)


if __name__ == "__main__":
    main()