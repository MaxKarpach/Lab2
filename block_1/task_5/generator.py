import random
from random import randint

file = open("input.txt", "w")

for i in range(random.randint(1, 5000)):
    file.write(str(randint(1,1000)) + " ")

file.close()
