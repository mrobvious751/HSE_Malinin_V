uchastnik_spora = [
{"name": 'ООО "Рога и Копыта"', "status": "Истец", "inn": "4545454545"},
{"name": 'Баширов А.А.', "status": "Ответчик", "inn": "32323232323232"},
{"name": 'Петров А.А.', "status": "Третье лицо", "inn": "12121212121212"}
]

name = input("Введите имя участника спора: ")
status = input("Введите статус участника спора (Истец/Ответчик/Третье лицо): ")
inn = input("Введите ИНН участника спора: ")


new_uchastnik = {"name": name, "status": status, "inn": inn}

uchastnik_spora.append(new_uchastnik)

print(uchastnik_spora)


    if sec == sec.isdigit():
        min = int(sec) / 60
        hour = int(min) / 60
        print(sec)
        print(min)
        print(hour)
    else:
        print("Попробуй еще раз")
