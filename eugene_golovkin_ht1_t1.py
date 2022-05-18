# знаю, что код огромен, но я был очень рад когда он заработал, поэтому оставил так:)
duration = int(input('Введите число: '))
seconds = 0
minutes = 0
hours = 0
days = 0
if duration < 60:
    seconds = duration
    print(str(seconds) + ' сек')
elif duration >= 60 and duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(str(minutes) + ' мин ' + str(seconds) + ' сек')
elif duration >= 3600 and duration < 86400:
    hours = duration // 3600
    minutes = duration % 3600 // 60
    seconds = duration % 60
    print(str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек')
elif duration >= 86400:
    days = duration // 86400
    hours = duration % 86400 // 3600
    minutes = duration % 3600 // 60
    seconds = duration % 60
    print(str(days) + ' дн ' + str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек')
