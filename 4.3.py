def main():
    a = int(input())
    b = int(input())
    for i in range(a, 32, b):
        print(i, end=" ")


if __name__ == "__main__":
    main()