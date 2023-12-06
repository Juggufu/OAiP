import random

answer = [
    'Да',
    'Нет',
    'Скорее всего да',
    'Скорее всего нет',
    'Возможно',
    'Имеются перспективы',
    'Вопрос задан неверно',

]
question = input()

print(random.choice(answer))