def main():
    n = False
    d = "0123456789"
    a = input("+")
    for d in a:
        n = True
        break
    if a:
        print("ok")
    else:
        print("Неправильный номер телефона")


if __name__ == "__main__":
    main()