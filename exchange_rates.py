import requests

body = requests.get('https://api.nbp.pl/api/exchangerates/tables/A/?format=json')
response = body.json()
rates = response[0]['rates']

my_dict = {}
for item in rates:
    my_dict[item["code"].lower()] = item["mid"]


def display_the_full_list_of_currencies():
    while True:
        display = input("Do you want to see the full list of available currencies with their codes? \nType Yes or No: ")
        display = display.lower()
        if display not in ("yes", "no"):
            print("Didn't get it. Please check your answer.")
            continue
        elif display == "yes":
            for item in rates:
                print(item["currency"])
                print(item["code"])
                print("-" * 10)
            break
        else:
            break


def do_you_want_to_continue():
    while True:
        choice = input("Do you want to continue? Type Yes or No: ")
        choice = choice.lower()
        if choice not in ("yes", "no"):
            print("Didn't get it. Please check your answer.")
            continue
        elif choice == "yes":
            return True
        else:
            print("Thanks, see you soon!")
            return False


display_the_full_list_of_currencies()

while True:
    currency = input("Enter a currency code: ")
    currency = currency.lower()
    if currency in my_dict:
        print(my_dict[currency])
        want_to_continue = do_you_want_to_continue()
        if not want_to_continue:
            break
    else:
        print("Please check if the entered code is correct and try again.")
        continue