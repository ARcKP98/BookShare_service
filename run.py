
import gspread
import pyfiglet
from colorama import Fore, Style
import pandas as pd
from pprint import pprint
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bookkeeping')

book = SHEET.worksheet('Biographies')
data = book.get_all_values()
data1 = data[1:]

pprint(data1)


def introduction():
    big_banner = pyfiglet.figlet_format("Bookkeeping Service!!")
    print(Fore.YELLOW + Style.BRIGHT + big_banner)
    # print(Style.RESET_ALL)
    print("Welcome to the Bookkeeping Service. We are glad you are here.\n")
    print("This service was built to allow people to share their books.\n")
    print("We have a collection of books for you to check-out, " +
          "if you just want a book to read.\n")
    print("We hope this service can be of use to you.\n")


def user_input():
    while True:
        name = input("What is your name(at least 3 characters): ").capitalize()
        if len(name) < 3:
            print("\nA minimum of three character is required(EG: Tim)."
                  "Please try again.")
            continue
        elif name.isdigit():
            print("You have a number in your name. Please enter your name.")
            continue
        return name


# def display_shot(show_books):
#     gen1 = SHEET.worksheet('sci-fi').get_all_values()
#     data = pd.DataFrame(gen1)
#     print(data)


def purpose(user_input):
    print(f"\n Hi {user_input}. What would you like to do?")
    print("\n 1. Check out our books. \
        \n 2. Donate a Book.\n")
    while True:
        try:
            choice = int(input("\n Make your choice: "))
            if choice == 1:
                print("\n You would like to see our collection.")
                show_books()
                break
            elif choice == 2:
                print("\n You would like to donate a book. How nice!")
                break
            elif choice:
                print("\n Enter a number from the given options.")
                continue
        except ValueError:
            print("\n Not a number")
            continue


def show_books():
    print("To view our collection, pick a genre: \
        \n 1. Science Fiction \
        \n 2. Biographies \
        \n 3. Self-Help")
    while True:
        try:
            choice = choice = int(input("\n Make your choice: "))
            if choice == 1:
                print("Loading.......")
                print("\n Here are our Science Fiction titles:\n")
                gen1 = SHEET.worksheet('sci-fi').get('B:C')
                data = pd.DataFrame(gen1)
                print(data.to_string(index=False, header=False))
                # gen1 = SHEET.worksheet('sci-fi')
                # # data1 = gen1[1:4]
                # print(gen1)
                break
            if choice == 2:
                print("Loading.......")
                print("Here are our biographical titles:")
                gen2 = SHEET.worksheet('Biographies').get('B:C')
                data = pd.DataFrame(gen2)
                print(data.to_string(index=False, header=False))

                # for col in gen1:
                #     for row in col:
                #         print(str(row).rjust(50), end="")
                #         print("")
                # data = pd.DataFrame(gen1)
                # print(data)
                break
            if choice == 3:
                print("Loading.......")
                print("\nHere are our Self-Help titles:")
                gen3 = SHEET.worksheet('Self-help').get('B:C')
                data = pd.DataFrame(gen3)
                print(data.to_string(index=False, header=False))

                break
            else:
                print("Please pick from one of the options provided.")
                continue
        except ValueError:
            print("Please enter a number.")
    return choice


def main():
    introduction()
    purpose(user_input())
    # display_shot(show_books())


main()
