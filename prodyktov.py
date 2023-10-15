def main():
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

if __name__ == "__main__":
   main()
