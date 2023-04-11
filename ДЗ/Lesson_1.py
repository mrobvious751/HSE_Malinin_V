#ДЗ 1
#2
# Первый способ решения
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

# Второй способ решения
while True:
    sec = input("Введите число в секундах: ")
    if sec.isdigit():
        min = int(sec) / 60
        hour = int(min) / 60
        print(sec)
        print(min)
        print(hour)
        break
    else:
        print("Попробуй еще раз")
        continue

#3
while True:
    n = input('Введите число от 1 до 9: ')
    if n.isdigit():
        n = int(n)
        if 1 <= n <= 9:
            n = str(n)
            nn = str(n) + str(n)
            nnn = str(n) + str(n) + str(n)
            print(int(n) + int(nn) + int(nnn))
            break
        else:
            print("Ты ввел число не от 1 до 9")
            continue
    else:
        print("Введи число от 1 до 9, а не текст")
        continue