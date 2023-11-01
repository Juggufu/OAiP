def main():
    a = int(input())
    b = []
    for i in range(a):
        b.append(input())
    for i in range(a):
        print(b[i], i + 1)


if __name__ == "__main__":
    main()
