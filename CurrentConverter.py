from forex_python.converter import CurrencyRates

def currency_converter():
    # Create a CurrencyRates object
    c = CurrencyRates()

    while True:
        # Get and display the list of available currencies
        currencies = c.get_rates('USD')
        print("Available currencies:")
        for currency, rate in currencies.items():
            print(f"{currency}: {rate}")
        # Get user input for conversion
        from_currency = input("Enter original currency code (or 'exit' to end): ").upper()
        # Exit Statement
        if from_currency == 'EXIT':
            break
        to_currency = input("Enter target currency code: ").upper()
        amount = float(input("Enter the amount to convert: "))
        # Perform currency conversion
        if from_currency == 'USD' and to_currency != 'USD':
            conversion_rate = currencies.get(to_currency)
            converted_amount = amount * conversion_rate
        elif from_currency == 'USD' and to_currency == 'USD':
            converted_amount = amount
        elif from_currency != 'USD' and to_currency == 'USD':
            conversion_rate = 1 / currencies.get(from_currency)
            converted_amount = amount * conversion_rate
        else:
            conversion_rate = (1 / (currencies.get(from_currency))) * currencies.get(to_currency)
            converted_amount = amount * conversion_rate
        # Display the result
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")


currency_converter()
