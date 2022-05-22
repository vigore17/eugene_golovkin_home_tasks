position_and_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
greetings = 'Привет'

for rem_elem in position_and_names:
    rem_elem = rem_elem.split()
    name = rem_elem.pop()
    print(f"'{greetings}, {name.lower() and name.capitalize()}!'")
