# -- IMPORTS --
import requests

# -- Short list of keywords for things that arent pulled from frankfurter
keywords = {
    "great": "GBP",
    "britain": "GBP",
    "uk": "GBP",
    "england": "GBP",
    "quid": "GBP",
    "sterling": "GBP",

    "america": "USD",
    "usa": "USD",
    "us": "USD",
    "buck": "USD",

    "europe": "EUR",
    "euro": "EUR",

    "australia": "AUD",
    "aus": "AUD",

    "canada": "CAD",
    "loon": "CAD",

    "turky": "TRY",

    "japan": "JPY",

    "crown": "CZK",
    "kron": "CZK",

    "crown": "DKK",
    "kron": "DKK",

    "crown": "NOK",
    "kron": "NOK",

    "zlot": "PLN",

    "kiwi": "NZD",

    "china": "CNY",

    "india": "INR",

    "south africa": "ZAR"
}

currenciesListURL = "https://api.frankfurter.app/currencies"




def get_currencies():
    return requests.get(currenciesListURL).json()

def find_currency(user_input, currencies, allow_retry = True):
    user_input = user_input.strip().lower()

    # -- Match by name --
    matches = \
        [(code, name) for code, name in currencies.items()
        if user_input in name.lower()]

    for keyword, code in keywords.items():
        if keyword in user_input:
            keyword_add = (code, currencies[code])
            if keyword_add not in matches:
                matches.append(keyword_add)

    # -- Match by code --
    if user_input.upper() in currencies:
        code = user_input.upper()
        print(f"{currencies[code]}, Code {code}")
        return code

    # -- What runs if matches --
    if matches:
        # -- Runs if multiple matches --
        if (len(matches) > 1):
            for i in range(len(matches)):
                code, name = matches[i]
                print(f"{name}, Code {code}")
            final_code = input("Multiple matches found. Please input chosen: ")
            result = find_currency(final_code, currencies, False)
            if result:
                return result
            else:
                return None
        else:
            code, name = matches[0]
            print(f"{name}, Code {code}")
            return code

    # -- If no match --
    print("Currency not found")

    if allow_retry:
        while True:
            retry = input("Try again? (y/n): ").lower()
            if retry == "y":
                new_input = input("Currency: ")
                result = find_currency(new_input, currencies, False) # -- No Retry --
                if result:
                    return result
            elif retry == "n":
                return None
