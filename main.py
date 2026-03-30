# Currency Converter - Converting currencies, getting accurate prices from scraping.

# -- Imports --
import conversion
from search import find_currency, get_currencies
from datetime import datetime

def get_date():
    while True:
        user_input = input("Please enter date in form YYYY-MM-DD: ")

        try:
            checked_date = datetime.strptime(user_input, "%Y-%m-%d")
            if checked_date > datetime.now():
                print("Date cannot be in the future.")
                continue
            return user_input
        except ValueError:
            print("Invalid date format. Please try again.")

def date_user_friendly(date):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"]
    day = date[8:]
    month = date[:7]
    month = month[5:]
    month_int = int(month)
    year = date[:4]
    month_name = months[month_int - 1]
    if (day == "11") or (day == "12") or (day == "13"):
        day_suffix = "th"
    elif (day[1] == "1"):
        day_suffix = "st"
    elif (day[1] == "2"):
        day_suffix = "nd"
    elif (day[1] == "3"):
        day_suffix = "rd"
    else:
        day_suffix = "th"
    if day[0] == "0":
        day = day[1]

    day = day + day_suffix
    user_friendly_date = day + " of " + month_name + " " + year
    return user_friendly_date

# -- Runs on file open --
if __name__ == "__main__":
    # -- Loop, whilst error checking input -- (Could have more error checking)
    finished = False
    currencies = get_currencies()
    while not finished:
        try:
            # -- Searching and validating currency codes --
            from_currency_search = input("Currency From: ")
            #fromCurrency = search.findCountryByName(fromCurrencySearch, True)
            from_currency = find_currency(from_currency_search, currencies)

            to_currency_search = input("Currency To: ")
            #toCurrency = search.findCountryByName(toCurrencySearch, True)
            to_currency = find_currency(to_currency_search, currencies)

            amount = float(input("Amount (Plain Number): "))
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            finished = True
        except ValueError:
            print("One or more invalid arguments.")

    # -- API Calls --
    finished = False
    while not finished:
        try:
            conversion_type = int(input("Please chose conversion type:\n1.Current\n2.Historic Value\n3.Rates Graph\n : "))
        except ValueError:
            print("invalid argument. ")
        try:
            if conversion_type == 1:
                converted = conversion.convertNow(from_currency, to_currency, amount)
                print(f"{amount} {from_currency} = {converted} {to_currency}")
                finished = True
            elif conversion_type == 2:
                date = get_date()
                user_friendly_date = date_user_friendly(date)
                converted = conversion.historicConvert(from_currency, to_currency, amount, date)
                print(f"{amount} {from_currency} was equal to ~{converted} {to_currency} on the {user_friendly_date}.")
                finished = True
            elif conversion_type == 3:
                conversion.ratesOverTime(from_currency,to_currency, amount)
                finished = True

        except ValueError:
            print("Please try again.")
