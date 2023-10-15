def main():
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

if __name__ == "__main__":
    main()
