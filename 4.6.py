def main():
    a = "аяоёэеуюыи"
    b = input()
    v = k = z = 0
    n = 1
    for w in b:
        if w in a:
            if n:
                z += 1
            k += 1
            n = 0
        elif w == ' ':
            n = 1
            if k:
                v += k
                k = 0
    print(v - z + k)


if __name__ == "__main__":
    main()

