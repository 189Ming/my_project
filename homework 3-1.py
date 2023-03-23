numbers = [2, 25, 13, 25, 6, 4]
size = 6
index = 0
avg = 0
sum = 0
while (index < size):
  sum = sum + numbers[index]
  index = index + 1
avg = sum / size
print(avg)