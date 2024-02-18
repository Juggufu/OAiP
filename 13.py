def template(a, b, c):
    p = a + b + c
    p2 = p / 2
    if p2 > a and p2 > b and p2 > c:
        print(f'Периметр: {p}')
        print(f'Площадь: {(p2 * (p2 - a) * (p2 - b) * (p2 - c)) ** 0.5}')
        print(f'Равнобедренный: {"ДА" if a == b or b == c or a == c else "НЕТ"}')
        print(f'Равносторонний: {"ДА" if a == b == c else "НЕТ"}')
    else:
        print(None)


template(5, 4, 5)
template(2, 1, 3)


def func_table(exp, x, y):
    res = [[eval(exp.replace('x', str(i)).replace('y', str(j))) for j in range(y + 1)] for i in range(x + 1)]
    [print(*i, sep='\t') for i in res]


func_table('x ** 2 + y', 3, 5)