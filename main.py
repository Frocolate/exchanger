# Currency Converter - Converting currencies, getting accurate prices from scraping.

currencies = [
    ("AFGHANISTAN", "Afghani", "AFN"),
    ("ALBANIA", "Lek", "ALL"),
    ("ALGERIA", "Algerian Dinar", "DZD"),
    ("AMERICAN SAMOA", "US Dollar", "USD"),
    ("ANDORRA", "Euro", "EUR"),
    ("ANGOLA", "Kwanza", "AOA"),
    ("ANGUILLA", "East Caribbean Dollar", "XCD"),
    ("ANTIGUA AND BARBUDA", "East Caribbean Dollar", "XCD"),
    ("ARGENTINA", "Argentine Peso", "ARS"),
    ("ARMENIA", "Armenian Dram", "AMD"),
    ("ARUBA", "Aruban Florin", "AWG"),
    ("AUSTRALIA", "Australian Dollar", "AUD"),
    ("AUSTRIA", "Euro", "EUR"),
    ("AZERBAIJAN", "Azerbaijanian Manat", "AZN"),
    ("BAHAMAS", "Bahamian Dollar", "BSD"),
    ("BAHRAIN", "Bahraini Dinar", "BHD"),
    ("BANGLADESH", "Taka", "BDT"),
    ("BARBADOS", "Barbados Dollar", "BBD"),
    ("BELARUS", "Belarussian Ruble", "BYN"),
    ("BELGIUM", "Euro", "EUR"),
    ("BELIZE", "Belize Dollar", "BZD"),
    ("BENIN", "CFA Franc BCEAO", "XOF"),
    ("BERMUDA", "Bermudian Dollar", "BMD"),
    ("BHUTAN", "Ngultrum", "BTN"),
    ("BHUTAN", "Indian Rupee", "INR"),
    ("BOLIVIA", "Boliviano", "BOB"),
    ("BOLIVIA", "Mvdol", "BOV"),
    ("BRAZIL", "Brazilian Real", "BRL"),
    ("CANADA", "Canadian Dollar", "CAD"),
    ("CHINA", "Yuan Renminbi", "CNY"),
    ("CROATIA", "Euro", "EUR"),
    ("CUBA", "Peso Convertible", "CUC"),
    ("CUBA", "Cuban Peso", "CUP"),
    ("CZECH REPUBLIC", "Czech Koruna", "CZK"),
    ("DENMARK", "Danish Krone", "DKK"),
    ("EGYPT", "Egyptian Pound", "EGP"),
    ("FRANCE", "Euro", "EUR"),
    ("GERMANY", "Euro", "EUR"),
    ("GHANA", "Ghana Cedi", "GHS"),
    ("GREECE", "Euro", "EUR"),
    ("HONG KONG", "Hong Kong Dollar", "HKD"),
    ("HUNGARY", "Forint", "HUF"),
    ("ICELAND", "Iceland Krona", "ISK"),
    ("INDIA", "Indian Rupee", "INR"),
    ("INDONESIA", "Rupiah", "IDR"),
    ("IRELAND", "Euro", "EUR"),
    ("ISRAEL", "New Israeli Sheqel", "ILS"),
    ("ITALY", "Euro", "EUR"),
    ("JAPAN", "Yen", "JPY"),
    ("KENYA", "Kenyan Shilling", "KES"),
    ("MEXICO", "Mexican Peso", "MXN"),
    ("NETHERLANDS", "Euro", "EUR"),
    ("NEW ZEALAND", "New Zealand Dollar", "NZD"),
    ("NIGERIA", "Naira", "NGN"),
    ("NORWAY", "Norwegian Krone", "NOK"),
    ("PAKISTAN", "Pakistan Rupee", "PKR"),
    ("PHILIPPINES", "Philippine Peso", "PHP"),
    ("POLAND", "Zloty", "PLN"),
    ("PORTUGAL", "Euro", "EUR"),
    ("QATAR", "Qatari Rial", "QAR"),
    ("ROMANIA", "Romanian Leu", "RON"),
    ("RUSSIAN FEDERATION", "Russian Ruble", "RUB"),
    ("SAUDI ARABIA", "Saudi Riyal", "SAR"),
    ("SINGAPORE", "Singapore Dollar", "SGD"),
    ("SOUTH AFRICA", "Rand", "ZAR"),
    ("SOUTH KOREA", "Won", "KRW"),
    ("SPAIN", "Euro", "EUR"),
    ("SRI LANKA", "Sri Lanka Rupee", "LKR"),
    ("SWEDEN", "Swedish Krona", "SEK"),
    ("SWITZERLAND", "Swiss Franc", "CHF"),
    ("THAILAND", "Baht", "THB"),
    ("TURKEY", "Turkish Lira", "TRY"),
    ("UKRAINE", "Hryvnia", "UAH"),
    ("UNITED ARAB EMIRATES", "UAE Dirham", "AED"),
    ("UNITED KINGDOM", "Pound Sterling", "GBP"),
    ("UNITED STATES", "US Dollar", "USD"),
    ("VIET NAM", "Dong", "VND"),
    ("ZAMBIA", "Zambian Kwacha", "ZMW"),
    ("ZIMBABWE", "Zimbabwe Dollar", "ZWL"),
]

def findCountryByName(name):
    return [c for c in currencies if name.lower() in c[0].lower()]

import requests
from bs4 import BeautifulSoup

def convertURL(URL, Currency1, Currency2):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    extracted = soup.find(class_='text-lg font-semibold text-xe-neutral-900 md:text-2xl')
    extracted = str(extracted)


    start = "=<!-- --> <!-- -->"
    end = '<span class='

    startParse = extracted.find(start)
    endParse = extracted.find(end)

    endString = extracted[:(endParse)]
    endString = endString[(startParse+18):]
    print(f"1 {Currency1} = ~{endString} {Currency2}.")

finished = False

baseURL = "https://www.xe.com/currencyconverter/convert/?Amount=1&From="
currencyList = input("Type yes to find currencies.")
while finished == False:
    if (currencyList.lower()) == 'yes':
        country = input("Input start / country name. ")
        result = findCountryByName(country)
        print(result)
        cont = input("Another? (y/n) ")
        if cont == "n": finished = True

fromCurrency = input("Currency From: ")
toCurrency = input("Currency To: ")

URL = (baseURL + fromCurrency + "&To=" + toCurrency)

convertURL(URL, fromCurrency, toCurrency)

