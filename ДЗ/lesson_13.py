python
import requests
from bs4 import BeautifulSoup


class ParserCBRF:
    def __init__(self):
        self.url_template = 'https://www.cbr.ru/hd_base/KeyRate/?UniDbQuery.Posted=True&UniDbQuery.' \
                            'From={start_date}&UniDbQuery.' \
                            'To={end_date}'

        self.start_date = '01.06.2023'
        self.end_date = '09.06.2023'

    @staticmethod
    def __render_dict(result_list):
        result_dict = {}
        for i in range(0, len(result_list), 2):
            result_dict[result_list[i]] = result_list[i + 1]
        return result_dict

    def __get_page(self):
        url = self.url_template.format(start_date=self.start_date, end_date=self.end_date)

        resp = requests.get(url).text
        return resp

    def start(self):
        html = self.__get_page()
        soup = BeautifulSoup(html, 'html.parser')
        result_list = [value.text for value in soup.find('table', 'data').find_all('td')]
        result_dict = ParserCBRF.__render_dict(result_list)
        return result_dict


pars = ParserCBRF()
print(pars.start())