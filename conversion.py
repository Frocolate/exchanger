import requests
import matplotlib.pyplot as plt
import numpy as np

# -- All calls to API in here --

# -- Exchange Rate at latest time --
def convert_now(from_currency, to_currency, amount):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    data = requests.get(url).json()
    converted = data["rates"][to_currency]
    return converted
    #print(f"{amount} {from_currency} = {converted} {to_currency}")

# -- Exchange Rate history --
def graph_over_time(from_currency, to_currency, amount, start_date, end_date):
    date_start = start_date
    date_end = end_date
    url = f"https://api.frankfurter.app/{date_start}..{date_end}?from={from_currency}&to={to_currency}"
    data = requests.get(url).json()

    # -- Blank sets for points to be added --
    x_points = []
    y_points = []
    seen_years = []

    # -- Graphing --
    for date, value in data["rates"].items():
        # -- Clean date
        concat_date = date[:4]
        if concat_date not in seen_years:
            x_points.append(concat_date)
            y_points.append(value[to_currency])
        #print(date, value[to_currency])
        seen_years.append(concat_date)
    x_graph = np.array(x_points)
    y_graph = np.array(y_points)
    plt.xticks(rotation=315)
    plt.plot(x_graph,y_graph)
    plt.xlabel("Year")
    plt.ylabel(f"Exchange Rate ({from_currency} > {to_currency})")
    plt.show()


# -- Will be Historical Exchange Rate
# -- One value, say GBP to USD on 01-01-1960
def historic_convert(from_currency, to_currency, amount, date):
    try:
        url = f"https://api.frankfurter.app/{date}"

        data = requests.get(url).json()
        converted = (data["rates"][to_currency])
        converted = converted * amount
        return converted
        #print(f"{amount} {from_currency} = {converted} {to_currency}")
    except:
        print("Please try again.")