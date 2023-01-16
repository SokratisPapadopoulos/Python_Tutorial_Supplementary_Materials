lst = [15, 32, 6, 24, 53, 41, 92, 2]
largest = lst[0]

for num in lst:
    if num > largest:
        largest = num
print(largest)
