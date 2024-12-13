import cProfile
import functools


@functools.lru_cache()
def filter_numbers():
    while True:
        try:
            number = int(input('введите число больше нуля: '))
            if number > 0:
                break
            else:
                print('введите число больше нуля: ')
        except ValueError:
            print('число должно быть целым')

    return [i for i in range(number+1) if i % 3 == 0 or i % 5 == 0]



cProfile.run('filter_numbers()')