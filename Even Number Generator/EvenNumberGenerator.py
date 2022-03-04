def all_even():
    n = 0
    while True:
        yield n
        n += 2

even = all_even()
x = int(input("Enter number:"))
print(', '.join(str(next(even)) for _ in range(x)))
