def square_of_sequence(x):
    for i in range(x):
        yield i*i

a = int(input("Enter Number:"))

gen=square_of_sequence(a)
while True:
    try:
        print (next(gen))
    except StopIteration:
        break
