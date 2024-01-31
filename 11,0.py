# 1
# import random
#
# f = open('lines.txt', encoding='utf-8')
# data = f.read()
# lines = data.split('\n')
# line = random.randrange(len(lines))
# print(lines[line])


# 2
f = open("lines.txt")
price = 0
for i in f:
    i = i.split('\t')
    price += eval(i[2]) * eval(i[1])
print(price)

# 3


# 4
# f = open('lines.txt', encoding='utf-8')
# data = f.read()
# lines = data.split('\n')
# max_lenght = len(max(lines, key=len))
# sought_words = [word for word in lines if len(word) == max_lenght]
# print(*sought_words)


# 5
# import os
#
# def file_size(name):
#     try:
#         with open(name, 'r') as file:
#             size = os.path.getsize(name)
#             return size
#     except FileNotFoundError:
#         return 0
#
#
# input_filename = 'input.txt'
# f_size = file_size(input_filename)
#
# if f_size > 0:
#     characters_count = f_size // 8
#     file_size_kb = f_size / 1024
#     print(f'В файле {input_filename} содержится {characters_count} символов')
#     print(f'Размер файла в КБ: {input_filename} ')
# else:
#     print(f'Файл имеет нудевой размер')