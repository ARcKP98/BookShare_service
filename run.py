
import gspread
import pyfiglet
from colorama import Fore, Style
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


def show_books():
    print("To view our collection, pick a genre: \
        \n 1. Science Fiction \
        \n 2. Biographies \
        \n 3. Self-Help")


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


def purpose(user_input):
    print(f"\n Hi {user_input}. What would you like to do?")
    print("\n 1. Check out our books. \
        \n 2. Donate a Book.\n")
    choice = int(input("\n Make your choice: "))

    if choice == 1:
        print("You would like to see our collection.")
        show_books()
    elif choice == 2:
        print("You would like to donate a book. How nice!")
    else:
        print("Please enter a number/")


def main():
    introduction()
    purpose(user_input())


main()
