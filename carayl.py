def main():
    s = int(input())
    while s != 0:
        if s % 3 == 0 and s % 7 == 0:
            print("Караул!")
            break
        elif s % 3 == 0:
            print("несчастливое")
        elif s % 7 == 0:
            print("опасное")
        else:
            print(s)
        s = int(input())


if __name__ == "__main__":
    main()