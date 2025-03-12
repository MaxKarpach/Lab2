import time
t_start = time.perf_counter()

input_file = open("input.txt", "r")
numbers = list(map(int, input_file.readline().split()))
input_file.close()

index_hirsha = 0
for i in range(len(numbers)):
    counter = 0
    for j in range(len(numbers)):
        if numbers[j] > index_hirsha:
            counter += 1
        if counter > index_hirsha:
            index_hirsha += 1
            break

print("Index Hirsha: %s. \n"
      "Time spend: %s seconds." % (index_hirsha, time.perf_counter()-t_start))
