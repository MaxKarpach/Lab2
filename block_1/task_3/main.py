import time
t_start = time.perf_counter()

input_file = open("input.txt", "r")
info = list(map(int, input_file.readline().split()))
total = info[0]
dist = info[1]
result = "none"

numbers = list(map(int, input_file.readline().split()))
input_file.close()

if total >= dist:
      for i in range(0,total):
            for j in range(i,total,dist):
                  if numbers[i] > numbers[j]:
                        change = numbers[i]
                        numbers[i] = numbers[j]
                        numbers[j] = change

for k in range(total-1):
      if numbers[k] > numbers[k+1]:
            result = "no"
            break
      else: result = "yes"
r = open("output.txt", "w")
r.write(result)
r.close()
print("Result: %s. \n"
      "Time spend: %s seconds." % (result, time.perf_counter()-t_start))
