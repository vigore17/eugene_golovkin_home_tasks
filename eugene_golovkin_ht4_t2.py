import requests

def currency_rates(pare):
    currency_page = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if pare not in currency_page:
        return None

    native_currency = currency_page[currency_page.find('<Value>', currency_page.find(pare)) + 7:currency_page.find('</Value>', currency_page.find(pare))]
    return f"{native_currency}"




