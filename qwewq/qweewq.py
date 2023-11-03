def F(n):
    if n < 4:
        return 1
    if n > 3 and n % 2 == 0:
        return F(n - 1) + F(n - 2) + F(n - 3)
    if n > 3 and n % 2 != 0:
        return n


print(F(2054) - F(2052))
