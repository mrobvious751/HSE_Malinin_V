inn = 7806437825

def check_org_inn(inn: int) -> bool:
    lst = [int(i) for i in list(str(inn))]
    coefficients = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    r_1 = 0
    for index, el in enumerate(lst[:9]):
        coef = coefficients[index]
        # print(f"coef: {coef} | el: {el}")
        r_1 += coef * el
    r_2 = r_1 % 11
    r_3 = r_2 % 10 if r_2 > 9 else r_2
    return r_3 == lst[-1]


def check_fiz_inn(inn: int) -> bool:
    lst = [int(i) for i in list(str(inn))]
    coefficients = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    r_1 = 0
    for index, el in enumerate(lst[:11]):
        coef = coefficients[index]
        # print(f"coef: {coef} | el: {el}")
        r_1 += coef * el


    # Дописать

def check_inn(inn: int) -> bool:
    if len(str(inn)) == 10:
        result = check_org_inn(inn)
    else:
        result = check_fiz_inn(inn)
    return result

print(check_inn(inn))

