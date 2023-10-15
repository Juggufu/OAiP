def main():
    print("зарплата за месяц")
    zp = int(input())
    print("количество отработанных часов")
    time = int(input())
    a=zp * 0.01 * time
    print("размер премии", a)
if __name__ == "__main__":
    main()
