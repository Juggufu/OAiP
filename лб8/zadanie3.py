def nearby(data, places=1):
    return list(filter(lambda x: '0' * places in x, data))


data = ['111', '101101', '11000']
print(*nearby(data), sep='\n')