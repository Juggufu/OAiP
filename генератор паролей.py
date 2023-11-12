def main():
    from random import random, choice
    a = 'AEIOUBCDFGHJKLMNPQRSTVWXYZ'
    b = 'aeioubcdfghjklmnpqrstvwxyz'
    c = '!#$%&*+-=?@^_'
    d = '0123456789'
    al = a + b + c + d
    f = ''
    f += al
    password = ''
    for i in range(8):
        password += choice(f)
    print('\n', password, '\n', sep='')


if __name__ == "__main__":
    main()








