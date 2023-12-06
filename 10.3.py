def main():
    import random
    al = [
        'апельсин', 'банан', 'яблоко', 'драконийфрукт',
          'кошка', 'собака', 'корова', 'хомяк', 'кролик',
          'кукуруза', 'картошка', 'лук', 'морковка', 'помидор'
        ]
    print('Привет! Желаю приятно поиграть в игру "Виселица"')
    secret = random.choice(al)
    guesses = 'йуеоаыяиюё'
    terns = int(input('Сколько попыток вы хотите: '))
    while terns > 0:
        propysk = 0
        for letters in secret:
            if letters in guesses:
                print(letters, end=' ')
            else:
                print('_', end=' ')
                propysk += 1
        if propysk == 0:
            print('Молодец! Ты выиграл')
            break
        guess = input('Назовите букву: ')
        guesses += guess
        if guess not in secret:
            terns -= 1
            print('Не угадали, осталось попыток:', terns)
        if terns == 0:
            print('Загаданное слово:', secret)


if __name__ == '__main__':
    main()