import datetime as DT
from datetime import datetime as dt
from bs4 import BeautifulSoup
import requests
import json


class ParserCBRF:
    """Класс который создает json файл, и записывает в него данные по курсу валют с start_date -> end_date."""
    def __init__(self, start_date: str, end_date: str) -> None:
        self.url_template: str = 'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={date}'
        self.res: dict = {}
        self.date: None = None

        self.start_date_dt: dt.date = dt.strptime(start_date, '%d.%m.%Y').date()
        self.end_date_dt: dt.date = dt.strptime(end_date, '%d.%m.%Y').date()
        self.step: DT.timedelta = DT.timedelta(days=1)

    def __render_dict(self, date: dt.date, lst: list[list[str]]) -> None:
        """Метод в классе, который создает итоговый словарь со значениями."""
        result_dict: dict = {}
        for line in lst:
            digital_code, letter_code, value, currency_name, rate = line
            dct: dict[str: str] = {'letter_code': letter_code, 'value': value, 'currency_name': currency_name, 'rate': rate}
            result_dict[digital_code] = dct
        self.res[self.__dt_type_to_str_type(date)] = result_dict

    @staticmethod
    def __dt_type_to_str_type(date: dt.date) -> str:
        """Перевод datetime тип данных в str тип данных."""
        return dt.strftime(date, '%d.%m.%Y')

    def __get_page(self, date: dt.date) -> str:
        """Берет html код со страницы"""
        url: str = self.url_template.format(date=self.__dt_type_to_str_type(date))
        resp: str = requests.get(url).text
        return resp

    def start(self) -> None:
        """Главный метод, который управляет другими методами."""
        self.date: dt.date = self.start_date_dt
        while self.date <= self.end_date_dt:
            html: str = self.__get_page(self.date)
            soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
            lst: list[list[str]] = [value.text.split('\n')[1:-1] for value in soup.find('tbody').find_all('tr')][1:]
            self.__render_dict(date=self.date, lst=lst)
            self.date += self.step
        with open('parsed_data.json', 'w', encoding='UTF-8') as json_file:
            json.dump(self.res, json_file, ensure_ascii=False)


class MultiCBRF:
    @staticmethod
    def __dt_type_to_str_type(date: dt.date) -> str:
        return dt.strftime(date, '%d.%m.%Y')

    def __init__(self) -> None:
        self.path: str = 'parsed_data.json'
        self.res: None = None
        self.open()

    def open(self) -> None:
        with open(self.path, 'r', encoding='UTF-8') as json_file:
            self.res: dict[str: dict[str]: dict[str: str]] = json.load(json_file)

    def rates_by_date(self, date) -> dict[str: dict[str: str]]:
        dct: dict[str: dict[str: str]] = self.res.get(date, 'Not Found')
        return dct

    def last_rate(self) -> dict[str: dict[str: str]]:
        return self.res.get(max(self.res.keys(), key=lambda date: dt.strptime(date, '%d.%m.%Y').date()), 'Not Found')

    def range_rates(self, from_date, to_date) -> list[dict[str: dict[str: str]]]:
        from_date_dt: dt.date = dt.strptime(from_date, '%d.%m.%Y').date()
        to_date_dt: dt.date = dt.strptime(to_date, '%d.%m.%Y').date()
        step: DT.timedelta = DT.timedelta(days=1)
        date: dt.date = from_date_dt
        lst: list = []
        while date <= to_date_dt:
            lst.append(self.res.get(self.__dt_type_to_str_type(date)))
            date += step
        return lst


# Создаем json файл со значениями (24.05.2023 -> 24.06.2023)
pars = ParserCBRF(start_date='24.05.2023', end_date='24.06.2023')
pars.start()

# Обращается и возвращает нужные значения
multi = MultiCBRF()
print(multi.range_rates('22.06.2023', '24.06.2023'))

