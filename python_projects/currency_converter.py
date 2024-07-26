# from requests import get
# from pprint import PrettyPrinter


# BASE_URL = "https://api.freecurrencyapi.com/"
# API_KEY = "fca_live_hHLDojn2Sz0N4e1VRTW5U5udH2q2Ipal8muBf7C0"

# printer = PrettyPrinter()

# def get_currencies():
#     endpoint = f"api/v7/currencies?apiKey={API_KEY}"
#     url = BASE_URL + endpoint
#     data = get(url).json()['results']

#     data = list(data.items())
#     data.sort()

#     return data


# def print_currencies(currencies):
#     for name, currency in currencies:
#         name = currency['currencyName']
#         _id = currency['id']
#         symbol = currency.get("currencySymbol", "")
#         print(f"{_id} - {name} - {symbol}")


# def exchange_rate(currency1, currency2):
#     endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
#     url = BASE_URL + endpoint
#     data = get(url).json()

#     if len(data) == 0:
#         print('Invalid currencies.')
#         return

#     rate = list(data.values())[0]
#     print(f"{currency1} -> {currency2} = {rate}")

#     return rate


# def convert(currency1, currency2, amount):
#     rate = exchange_rate(currency1, currency2)
#     if rate is None:
#         return

#     try:
#         amount = float(amount)
#     except:
#         print("Invalid amount.")
#         return

#     converted_amount = rate * amount
#     print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
#     return converted_amount


# def main():
#     currencies = get_currencies()

#     print("Welcome to the currency converter!")
#     print("List - lists the different currencies")
#     print("Convert - convert from one currency to another")
#     print("Rate - get the exchange rate of two currencies")
#     print()

#     while True:
#         command = input("Enter a command (q to quit): ").lower()

#         if command == "q":
#             break
#         elif command == "list":
#             print_currencies(currencies)
#         elif command == "convert":
#             currency1 = input("Enter a base currency: ").upper()
#             amount = input(f"Enter an amount in {currency1}: ")
#             currency2 = input("Enter a currency to convert to: ").upper()
#             convert(currency1, currency2, amount)
#         elif command == "rate":
#             currency1 = input("Enter a base currency: ").upper()
#             currency2 = input("Enter a currency to convert to: ").upper()
#             exchange_rate(currency1, currency2)
#         else:
#             print("Unrecognized command!")

# main()

# # data = {'data': {'AUD': 1.5289901953,
# #           'BGN': 1.8021703129,
# #           'BRL': 5.6441808321,
# #           'CAD': 1.3819502488,
# #           'CHF': 0.8805201001,
# #           'CNY': 7.2302410614,
# #           'CZK': 23.3518740083,
# #           'DKK': 6.8769911048,
# #           'EUR': 0.9211701532,
# #           'GBP': 0.7778800808,
# #           'HKD': 7.804051316,
# #           'HRK': 6.5851110423,
# #           'HUF': 361.6460335721,
# #           'IDR': 16229.708889747,
# #           'ILS': 3.6794407166,
# #           'INR': 83.7182587328,
# #           'ISK': 137.9767622799,
# #           'JPY': 153.6906694154,
# #           'KRW': 1379.0131173185,
# #           'MXN': 18.4422236828,
# #           'MYR': 4.6612906633,
# #           'NOK': 11.0246217601,
# #           'NZD': 1.6981701834,
# #           'PHP': 58.5841162727,
# #           'PLN': 3.9458905961,
# #           'RON': 4.5784405144,
# #           'RUB': 84.9932052317,
# #           'SEK': 10.8243913813,
# #           'SGD': 1.3432802247,
# #           'THB': 36.1946254346,
# #           'TRY': 33.1479950449,
# #           'USD': 1,
#         #   'ZAR': 18.3467827443}}

