# Вариант b

def find_total(num):
    sum = 0
    while (num != 0):
        sum = sum + num % 10
        num = num // 10
    return sum

first_list = []
for number in range(1, 1001, 2):
    number = number ** 3 + 17
    first_list.append(number)

total_sum = 0
for num in first_list:
    find_total(num)
    if find_total(num) % 7 == 0:
        total_sum += find_total(num)

print(total_sum)
