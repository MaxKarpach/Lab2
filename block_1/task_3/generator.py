import random

file = open("input.txt", "w")

total = random.randint(1, 10**5)
file.write(str(total) + " " + str(random.randint(1, 10**5)) + '\n')

for i in range(total):
    file.write(str(random.randint(1, 10**9)) + " ")

file.close()
