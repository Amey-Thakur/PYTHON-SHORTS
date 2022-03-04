def fib(a=0, b=1):
    """Generator that yields Fibonacci numbers. `a` and `b` are the seed values"""
    while True:
        yield a
        a, b = b, a + b

f = fib()
x = int(input("Enter number:"))
print(', '.join(str(next(f)) for _ in range(x)))
