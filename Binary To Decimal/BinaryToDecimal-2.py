binary = input('Enter a Binary number: ')

#since binary base is 2, so pass 2 as 2nd argument
decimal = int(binary,2)

print("Decimal of {p} is {q} ".format(p=binary, q=decimal))
