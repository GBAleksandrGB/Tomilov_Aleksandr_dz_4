import decimal
import requests
from bs4 import BeautifulSoup


def args_lower_check(args):
    for i, arg in enumerate(args):
        if args[i].islower():
            args[i] = args[i].upper()
    return args


def currency_rates(*args):
    args = args_lower_check(list(args))
    rates_char = []
    rates_val = []
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    if response.status_code != 200:
        print(f'error: {response.status_code}')

    soup = BeautifulSoup(response.text.replace(',', '.'), 'html.parser')
    res_char = soup.find_all('charcode')
    res_val = soup.find_all('value')

    for tag in res_char:
        rates_char.append(tag.text)

    for tag in res_val:
        d = decimal.Decimal
        rates_val.append(d(tag.text).quantize(d('1.00')))

    rates = dict(zip(rates_char, rates_val))

    for i, arg in enumerate(args):
        if args[i] not in rates:
            return None, print('Неизвестно')
        else:
            print(f'Курс {args[i]}: {rates[args[i]]}')


currency_rates('usd', 'EUR')
