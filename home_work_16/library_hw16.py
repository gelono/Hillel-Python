from datetime import datetime

import requests


class ExchangeRate:
    HOST = 'https://bank.gov.ua/'
    END_POINT: str = 'NBUStatService/v1/statdirectory/exchange'
    currency: str = None
    date: str = None

    def __init__(self, date: str, currency: str = 'USD'):
        self.currency = currency
        self.date = date

    def get_current_rate(self):
        """
        This method returns a current currency rate
        :return: float
        """
        url = self.HOST + self.END_POINT + '?json'
        rate = 'No data'
        try:
            response = requests.get(url)
        except Exception as e:
            response = None
            print(e)

        if 300 > response.status_code >= 200:
            if 'application/json' in response.headers.get('Content-Type', ''):
                try:
                    data = response.json()
                except Exception as e:
                    print(e)
                else:
                    for dct in data:
                        if dct.get('cc') == self.currency:
                            rate = dct.get('rate', 'no data')
        return rate

    def get_rate_with_date(self):
        """
        This method returns a currency rate for the specified date
        :return: float
        """
        date = datetime.strptime(self.date, "%d-%m-%Y")
        date_for_filename = date.strftime('%d-%m-%Y')
        date = date.strftime('%Y-%m-%d')
        date = date.replace('-', '')
        url = f'{self.HOST}{self.END_POINT}?date={date}&json'
        try:
            response = requests.get(url)
        except Exception as e:
            response = None
            print(e)

        if 300 > response.status_code >= 200:
            if 'application/json' in response.headers.get('Content-Type', ''):
                try:
                    data = response.json()
                except Exception as e:
                    print(e)
                else:
                    currencies = []
                    rates = []
                    for dct in data:
                        currencies.append(dct.get('cc', 'no data'))
                        rates.append(dct.get('rate', 'no data'))
                    self._save_rate(date_for_filename, currencies, rates)

    @staticmethod
    def _save_rate(date, curr_list, rates_list):
        """
        This method saves info about rates into the file
        :param date: str
        :param curr_list: list
        :param rates_list: list
        :return:
        """
        date = date.replace('-', '_')
        with open(f'{date}.txt', 'w') as file:
            for index, currency, rate in zip(range(1, len(curr_list)+1), curr_list, rates_list):
                file.write(f'{index}. [{currency}] to UAH: [{rate}]' + '\n')
