def factorials_up_to(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a

b = int(input("Enter Number:"))
for x in factorials_up_to(b):
    print(x)
