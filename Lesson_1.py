#ДЗ 1


#2
sec = input('Введите количество секунд: ')

if not sec.isdigit():
    print("Ошибка: введено не число.")
else:
    sec = int(sec)
    min = sec/60
    hour = min/60
    print('Количество секунд: ', sec)
    print('Количество минут: ', min)
    print('Количество часов: ', hour)

#3
n = input('Введите число от 1 до 9: ')
nn = n + n
nnn = n + n + n
print(int(n) + int(nn) + int(nnn))