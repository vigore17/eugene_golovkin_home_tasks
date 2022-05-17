percent = int(input('Введите процент от 1 до 100: '))
first_list = [1, 21, 31, 41, 51, 61, 71, 81, 91]
second_list = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54, 62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
if percent in first_list:
    word = 'процент'
elif percent in second_list:
    word = 'процента'
else:
    word = 'процентов'
print(percent, word)