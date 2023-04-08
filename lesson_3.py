from data import repondents, courts

"""
{'address': '660020, КРАЙ КРАСНОЯРСКИЙ, Г. КРАСНОЯРСК, УЛ. 7-Й КМ ЕНИСЕЙСКОГО '
             'ТРАКТА, ТЕРРИТОРИЯ ЗАО "ТЗБ КРАЙПОТРЕБСОЮЗА"',
  'bankruptcy_id': '12182',
  'case_number': 'А33-2794/2011',
  'category': 'Обычная организация',
  'category_code': 'SimpleOrganization',
  'full_name': 'общество с ограниченной ответственностью " ПРОДСЕРВИС "',
  'inn': '2465081302',
  'ogrn': '1042402640125',
  'region': 'Красноярский край',
  'short_name': 'ООО " ПРОДСЕРВИС "'},
"""

"""
 'Ф06': {'court_address': '420066 Республика Татарстан, Казань,ул. '
                          'Красносельская, д. 20',
         'court_code': 'Ф06',
         'court_email': 'info@faspo.arbitr.ru',
         'court_fax_info': '(843)291-04-79',
         'court_head': 'Глазов Юрий Владимирович',
         'court_name': 'Поволжский арбитражного округ',
         'court_phone_info': '(843)291-04-13, 291-04-15',
         'court_time_shift': 0,
         'court_website': 'http://faspo.arbitr.ru/'},
"""

def run(string):
    # Арбитражного суда города Санкт-Петербурга
    words = string.split()[2::]
    text = 'Арбитражный суд'
    for i in words:
        text += f" {i}"
    return text

for full_info_request in repondents:
    case_number = full_info_request.get('case_number')
    if case_number:
        code_of_court, arr = case_number.split('-')
        full_info_court = courts.get(code_of_court)
        # ==============

        court = run(full_info_court.get('court_name'))
        address = full_info_court.get('court_address')
        name = full_info_request.get('full_name')
        otvetchik_inn = full_info_request.get('inn')


        # =============
        result = f"В {court}\n" \
                 f"Адресс: {address}\n" \
                 f"Истец: Малинин В.К.\n" \
                 f"ИНН Ответчика: {otvetchik_inn}"
        print(result)
        print('=' * 50)

