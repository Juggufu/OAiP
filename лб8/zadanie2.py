s = input('введите предложение: ').split()
print(*list(map(lambda x: x.rjust(len(max(s, key = len)), "*"), s)), sep = "\n")
