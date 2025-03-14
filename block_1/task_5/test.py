import time

file = open("input.txt", "r")
numbers = list(map(int, file.readline().split()))
file.close()

check = int(input())
counter = 0
for i in range(len(numbers)):
    if numbers[i] >= check: counter += 1

print(counter)
time.sleep(5)
