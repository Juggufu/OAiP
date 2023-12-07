def main():
     # 1
    a = input()
    if a == ("Python"):
        print("Да")
    else:
        print("Нет")
     # 2
    a = input()
    b = input()
    if a == "да" or a == "нет" and b == "да" or b == "нет":
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")
     # 3
    one = input()
    two = input()
    th = input()
    if (one == "1" or one == "один") and (two == "2" or two == "два") and \
            (th == "3" or th == "три"):
        print("Гори")
    else:
        print("НЕ Гори")
     # 4
    j = input()
    au = input()
    if j != au and (j == "Тула" and au != "Пенза" or au == "Пенза" and j != "Тула"):
        print("ДА")
    else:
        print("НЕТ")
     # 5
    n = int(input())
    m = int(input())
    print((n + m - 1) // m)
     # 6
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    suma = n1 + n3 // 8
    if suma != 0 and n2 == 3:
        print("Подходит")
    else:
        print(n1 + n3, " ", n2)
     # 7
    print("выберите категорию товара")
    eat = input()
    if eat == "продукты":
        print("введите цену:")
        prise = int(input())
        if prise < 100:
            print("Попробуйте нашу выпечку!")
        elif 99 < prise < 500:
            print("Как насчёт орехов в шоколаде?")
        elif prise > 499:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")
     # 8
    print("цена первого товара:")
    price_1 = int(input())
    print("цена второго товара:")
    price_2 = int(input())
    print("цена третьего товара:")
    price_3 = int(input())
    payment = price_1 + price_2 + price_3
    promotion = (price_1 + price_2 + price_3) / 2
    promotion_2 = (price_1 + price_2 + price_3) / 3
    if price_1 < price_2 < price_3:
        print("акция!!")
        print("К оплате:", promotion_2, )
    elif price_1 > price_2 > price_3:
        print("акция!!")
        print("К оплате:", promotion, )
    else:
        print("К оплате:", payment, )
     # 9
    print("введите число покупателей позавчера")
    piple = int(input())
    print("введите число покупателей вчера")
    piple_2 = int(input())
    segodna = piple_2 + (piple_2 - piple)
    vchera = piple_2 - (piple_2 - piple)
    if piple < piple_2:
        print("сегодня магазин посетит:", segodna,)
    elif piple_2 < piple:
        print("сегодня магазин посетит:", vchera,)
    else:
        print("я не могу решить")
      # 10
    year = int(input('Введите год: '))
    if year % 4 != 0:
        print('Год не високосный.')

    elif year % 100 == 0:
        if year % 400 == 0:
            print('Год високосный.')
        else:
            print('Год не високосный.')
    else:
        print('Год високосный.')
     # 11
    a = int(input())
    if a % 2 == 0:
        print('Четное')
    else:
        print('Нечетное')


if __name__ == '__main__':
    main()