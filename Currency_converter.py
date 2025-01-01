def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount')

def get_currency(direction):
    while True:
        currency = input(f'Enter {direction} currency (USD/PESO): ').upper()
        if currency in ['USD', 'PESO']:
            return currency
        print('Invalid currency. Please enter USD or PESO')

def convert(amount, source_currency, target_currency):
    PESO_TO_USD = 0.018  # Example rate: 1 peso = 0.018 USD
    USD_TO_PESO = 1 / PESO_TO_USD

    if source_currency == 'PESO' and target_currency == 'USD':
        return amount * PESO_TO_USD
    elif source_currency == 'USD' and target_currency == 'PESO':
        return amount * USD_TO_PESO
    return amount

def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    target_currency = get_currency('Target')
    converted_amount = convert(amount, source_currency, target_currency)
    print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')

if __name__ == "__main__":
    main()