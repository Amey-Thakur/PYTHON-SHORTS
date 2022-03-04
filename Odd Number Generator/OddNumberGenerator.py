def all_odd():
    n = 1
    while True:
        yield n
        n += 2

odd = all_odd()
x = int(input("Enter number:"))
print(', '.join(str(next(odd)) for _ in range(x)))
