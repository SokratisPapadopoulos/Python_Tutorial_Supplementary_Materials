lst = [2, 4, 6, 2, 8, 10, 4, 6, 12, 14]
distinct_list = []

for num in lst:
    if num not in distinct_list:
        distinct_list.append(num)

print(lst)
print(distinct_list)
