data_list = [('привет', 25, 'пока'),
             ('добро', 36, 'зло'),
             ('свет', 44, 'темнота'),
             ('сладкое', 10, 'соленое')]
sorted_1 = sorted(data_list, key=lambda x: x[2])
sorted_2 = sorted(data_list, key=lambda x: x[1])
# sorted_3 = data_list.sort(key=sortByLength)
sorted_4 = sorted(data_list, key=lambda x: x[1], reverse=True)
print(*sorted_1)
print(*sorted_2)
print(*sorted_4)