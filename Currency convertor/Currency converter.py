def currency_convertor(amount, from_currency, to_currency):
    rates = {
        "USD": 87.30,       #1 USD = 87.30 INR
        "EUR": 101.61,      #1 EUR = 101.61 INR
        "INR": 1            
    }
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in rates or to_currency not in rates:
        raise ValueError(f"Currency not supported: {from_currency} to {to_currency}")
    
    amount_in_inr = amount * rates[from_currency]
    converted = amount_in_inr / rates[to_currency]
    return converted

def main():
    print("Currency converter")
    try:
        amount = float(input("Enter amount: "))
        from_cur = input("From currency (USD/EUR/INR): ")
        to_cur = input("To currency (USD/EUR/INR): ")
        result = currency_convertor(amount, from_cur, to_cur)
        print(f"{amount} {from_cur.upper()} = {result} {to_cur.upper()}")
    except ValueError as ve:
        print(ve)
    except Exception:
        print("Invalid input. Please try again.")

main()      #ye nahi dala to run hi nahi honga code bahot important hai ye