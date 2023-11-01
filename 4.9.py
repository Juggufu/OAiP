def main():
    a = input()
    d = ""
    for i in a:
        if i.lower() in "аеёийоуыэюя":
            d += "0"
        else:
            d += "1"
    print(d)


if __name__ == "__main__":
    main()