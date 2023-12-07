def main():
    #  1
    pr = input()
    while pr != "":
        print(len(pr))
        pr = input()

    #  2
    no = 0
    chet = float(input())
    while chet <= 36.6:
        if chet < 0:
            no += 1
        chet = float(input())
    print(no)

    #  3
    mn = 0
    n = int(input())
    while 0 < n < 1000:
        if n > mn:
            mn = n
        n = int(input())
    print(mn)

    #  4
    i = 999999999
    a = 0
    nums = list(map(int, input().split()))
    print(nums)
    while a < len(nums):
        if nums[a] < i:
            i = nums[a]
        a += 1
    print(i)

    #  5
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

    #  6
    a = 0
    summa = 0
    while a < 1000:
        a += 1
        summa = (a * (a + 1) / 2)
        print(int(summa))

    #  7
    print("Большая коробка: ")
    x = int(input("Ширина: "))
    y = int(input("Длина: "))
    z = int(input("Высота: "))
    m_box = 0
    while True:
        print("Маленькая коробка: ")
        a = int(input("Ширина: "))
        b = int(input("Длина: "))
        c = int(input("Высота: "))
        if a == 0:
            break
        if a > x or b > y or c > z:
            print("Ошибка")
        else:
            m_box += 1
    print(m_box)

    #  8
    a = input()
    b = ''
    c = 99999999
    while a != 'стоп':
        if len(a) < c:
            b = a
            c = len(a)
        a = input()
    print(b)

    #  9
    n_1 = int(input())
    b = input()
    n_2 = int(input())
    while b != 'стоп':
        if b == '+':
            n_2 += n_1
        elif b == '-':
            n_2 -= n_1
        elif b == '*':
            n_2 *= n_1
        elif b == '/':
            n_2 /= n_1
        print(n_2)
        b = input()
        n_1 = int(input())

    #  10
    slova = ''
    while True:
        word = input()
        slova += word + ' '
        if word == 'стоп':
            break
        slova += word + ''
        if word.endswith('.') or word.endswith('!'):
            print(slova.split())
            slova = ''



if __name__ == "__main__":
    main()