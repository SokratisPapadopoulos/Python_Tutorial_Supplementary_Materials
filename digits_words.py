digits = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four'
}
output = ''
phone = input('phone: ')
for num in phone:
    output += digits.get(num, '!') + ' '

print(output)
