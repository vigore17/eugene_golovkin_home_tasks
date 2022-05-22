# к сожалению не со всеми условиями справился
weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(weather_list)):
    if '+' in weather_list[i]:
        weather_list[i] = f'"+{int(weather_list[i]):02d}"'
    elif weather_list[i].isdigit():
        weather_list[i] = f'"{int(weather_list[i]):02d}"'
weather_string = ' '.join(weather_list)
print(weather_string)
