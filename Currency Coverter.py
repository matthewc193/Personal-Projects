from requests import get 
from pprint import PrettyPrinter

BASE_URL = 'https://api.freecurrencyapi.com/v1/latest?apikey='
URL_NZD_TO_ALL = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_VqTsbPRC1eKngJLfEngvvz1JdBQqNDMbtm4yXqmh&currencies=AUD%2CBGN%2CBRL%2CCAD%2CCHF%2CCNY%2CCZK%2CDKK%2CEUR%2CGBP%2CHKD%2CHRK%2CHUF%2CIDR%2CILS%2CINR%2CISK%2CJPY%2CKRW%2CMXN%2CMYR%2CNOK%2CNZD%2CPHP%2CPLN%2CRON%2CRUB%2CSEK%2CSGD%2CUSD%2CZAR&base_currency=NZD'
API_KEY = 'fca_live_VqTsbPRC1eKngJLfEngvvz1JdBQqNDMbtm4yXqmh'
printer = PrettyPrinter()

currency_data_nzd =  get(URL_NZD_TO_ALL).json()['data']

print(currency_data_nzd)
def display_currencies():
    print('Foreign Currency in Terms of NZD')
    for key, rate in currency_data_nzd.items():
        print(f'{key} - {round(rate, ndigits=2)}')
        print('-----------------')

def get_rate(currency_base, currency_to):
    CUSTOM_URL = f'{BASE_URL}{API_KEY}&currencies={currency_to}&base_currency={currency_base}'
    currency_data =  get(CUSTOM_URL).json()['data']
    return currency_data[currency_to]

def convert_currency(currency_base, currency_to, amount):
    rate = get_rate(currency_base, currency_to)
    try:
        amount = float(amount)
    except:
        print('Invalid amount!')
        return
    
    converted_amount = rate * amount
    converted_amount = round(converted_amount, ndigits=2)
    print(f'{amount} in {currency_base} is worth {converted_amount} in {currency_to}')
    return converted_amount
    
def main():
    print('Welcome to currency converter')
    print('------------------------------')
    print('Commands:')
    print('List ~ Displays all available currencies')
    print('Rate ~ Get the exchange rate of two currencies')
    print('Convert ~ Convert from one currency to another\n')

    while True:
        command = input('Enter a command (enter q to quit): \n').lower()

        if command == 'list':
            display_currencies()
            print('\n')

        elif command == 'rate':
            base_currency = input('Enter a base currency: ')
            currency_to = input('Enter a currency to convert to: ')
            rate = get_rate(base_currency, currency_to)
            print(f'{base_currency} -> {currency_to} = {rate}\n')

        elif command == 'convert':
            base_currency = input('Enter a base currency: ')
            currency_to = input('Enter a currency to convert to: ')
            amount = input('Enter a base amount: ')
            convert_currency(base_currency, currency_to, amount)
            print('\n')

        elif command == 'q':
            break

        else:
            print('Invalid Command!\n')

main()

