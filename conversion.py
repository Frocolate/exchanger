import requests
# -- All calls to API in here --

# -- Exchange Rate at latest time --
def convertNow(from_currency, to_currency, amount):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    data = requests.get(url).json()
    converted = data["rates"][to_currency]
    return converted
    #print(f"{amount} {from_currency} = {converted} {to_currency}")

# -- Exchange Rate history --
# -- Will be graphical, graph for time and price --
def ratesOverTime(from_currency, to_currency, amount):
    date_start = str(input("Start Year: "))
    date_end = str(input("End Year: "))
    date_start = f'{date_start}-01-01'
    date_end = f'{date_end}-01-01'
    url = f"https://api.frankfurter.app/{date_start}..{date_end}?from={from_currency}&to={to_currency}"
    data = requests.get(url).json()

    # -- Display all values known by Frankfurter --
    print(f"Values shown are 1 {from_currency} to X {to_currency}")
    for date, value in data["rates"].items():
        print(date, value[to_currency])

# -- Will be Historical Exchange Rate
# -- One value, say GBP to USD on 01-01-1960
def historicConvert(from_currency, to_currency, amount, date):
    try:
        url = f"https://api.frankfurter.app/{date}"

        data = requests.get(url).json()
        converted = (data["rates"][to_currency])
        converted = converted * amount
        return converted
        #print(f"{amount} {from_currency} = {converted} {to_currency}")
    except:
        print("Please try again.")