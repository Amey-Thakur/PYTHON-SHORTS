import random

print("".join([chr(i) for i in random.choices(range(33, 126), k=15)]))