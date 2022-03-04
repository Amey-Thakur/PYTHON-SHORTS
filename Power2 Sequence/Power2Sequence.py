x = int(input("Enter Number: "))
result = list(map(lambda x: 2 ** x, range(x)))

for i in range(x):
   print("2 raised to power",i,"is",result[i])
