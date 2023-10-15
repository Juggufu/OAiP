def main():
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
  print("К оплате:", promotion_2,)
 elif price_1 > price_2 > price_3:
  print("акция!!")
  print("К оплате:", promotion,)
 else:
  print("К оплате:", payment,)
if __name__ == "__main__":
      main()
