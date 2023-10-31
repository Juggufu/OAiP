def main():
    no = 0
    chet = float(input())
    while chet <= 36.6:
        if chet < 0:
            no += 1
        chet = float(input())
    print(no)

if __name__ == "__main__":
    main()