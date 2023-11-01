def main():
    slova = ''
    while True:
        word = input()
        slova += word + ' '
        if word == 'стоп':
            break

if __name__ == "__main__":
    main()