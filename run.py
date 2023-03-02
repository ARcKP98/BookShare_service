'''
Importing the Google sheet API along with python libraries and module.
'''
import re
from time import sleep
import gspread
import pyfiglet
from colorama import Fore, Style
from tabulate import tabulate
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


def introduction():
    '''
    Informs users the purpose of this program.
    '''
    big_banner = pyfiglet.figlet_format("Bookkeeping Service!!")
    print(Fore.YELLOW + Style.BRIGHT + big_banner)
    print("Welcome to the Bookkeeping Service. We are glad you are here.\n")
    print("This service was built to allow people to share their books.\n")
    print("We have a collection of books for you to check-out,")
    print("if you just want a book to read.\n")
    print("We hope this service can be of use to you.\n")


def user_input():
    '''
    This function asks user for their name and checks if the user
    has inputted a proper name.
    '''
    while True:
        name = input("Enter your name(at least 3 characters):\n").capitalize()
        if len(name) < 3:
            print("\n A minimum of three character is required(EG: Tim)."
                  "Please try again.")
            continue
        elif name.isdigit():
            print("\n You have entered a number. Please enter your name.")
            continue
        return name


def purpose(name):
    '''
    This function helps user pick between browsing the collection and
    donating to the collection.
    '''
    print(f"\n Hi {name}. What would you like to do?")
    sleep(1)
    print("\n 1. Check out our books. \
        \n 2. Donate a Book.\n")
    while True:
        try:
            choice = int(input("\n Make your choice: \n"))
            if choice == 1:
                print("\n You would like to see our collection.\n")
                sleep(0.5)
                show_books()
                break
            elif choice == 2:
                print("\n You would like to donate a book. How nice!\n")
                sleep(0.5)
                donate()
                break
            elif choice:
                print("\n Enter a number from the given options.")
                continue
        except ValueError:
            print("\n Not a number")
            continue


def checkout():
    '''
    This function checks whether user input is valid and removes the book from
    the collection.
    '''

    sleep(1)
    print("\nIf you would like to borrow a book, enter the code of the book.")
    print("If you don't want to borrow a book and leave, press 0.\
        \n")
    decision = input("\n Make a choice: \n")
    pattern = re.compile(r'\b' + decision + r'\b')
    while True:
        try:
            if decision == str(0):
                while True:
                    opt = input("Are you sure you want to leave " +
                                "the program?(Yes/No):\n").capitalize()
                    if opt == ('Yes'):
                        print("Leaving the program...")
                        sleep(1)
                        print("\nGoodbye.\n")
                        quit()
                    elif opt == ('No'):
                        print(" \n Taking you back to the books list...\n")
                        sleep(0.5)
                        print("\nWelcome back.\n")
                        sleep(1)
                        show_books()
                    else:
                        print("Enter a valid input")
                        continue
            else:
                codes = SHEET.worksheet('Books')
                code = codes.find(pattern, in_column=1)
                row_info = codes.row_values(code.row)
                book = row_info[1]
                author = row_info[2]
                print(f"You chose the book {book} by {author}")
                sleep(0.8)
                print("Checking out...")
                sleep(3)

                codes.delete_rows(code.row)

                print("Checkout complete.")
                sleep(0.8)
                print("Good Bye")
                quit()

        except AttributeError:
            print("Please enter a number.")
            decision = input("\n Make a choice: \n")
            pattern = re.compile(r'\b' + decision + r'\b')


def donate():
    '''
    This function allows user to donate a book of their choice.
    It checks if the book is already in the collection and if
    it is not, it adds the book to the sheet.
    '''
    sleep(0.5)
    don = input("What is the name of the book?(The proper name):\n").title()
    don_reg = re.compile(r'\b' + don + r'\b')
    collection = SHEET.worksheet('Books')

    code = collection.find(don_reg, in_column=2)
    if code is None:
        sleep(1)
        print("We don't have this book.")
        sleep(0.5)
        chek_code = len(collection.get_all_values()) + 5
        book = don
        author = input("What is the Author's name?: \n").title()
        sleep(0.5)

        entry = []
        entry.append(chek_code)
        entry.append(book)
        entry.append(author)

        print("Adding the entry to the library...")
        sleep(3)
        collection.append_row(entry)
        print(f"You donated {book} by {author}.")
        print("Thank you for your donation!! Have a nice day.")
        quit()
    if code:
        row_info = collection.row_values(code.row)
        book = row_info[1]
        sleep(0.5)
        print(f"We have {book} in our collection.")
        sleep(0.5)
        while True:
            sel = input("\n Would you like to see the books we have?(Y/N): \n")
            if sel == 'Y' or sel == 'y':
                print("\n Returning to the collection.....")
                sleep(1)
                show_books()
                continue
            elif sel == 'N' or sel == 'n':
                while True:
                    sel = input("Would you like to leave the program?(Y/N):\n")
                    sleep(0.8)
                    if sel == 'Y' or sel == 'y':
                        print("Leaving the program...")
                        sleep(1.8)
                        print("GoodBye")
                        quit()
                    elif sel == 'N' or sel == 'n':
                        print("Taking you to the book collection...")
                        sleep(0.5)
                        show_books()
                        break


def show_books():
    '''
    This function displays all the books that are on the
    Google Sheets.
    '''
    sleep(1.8)
    print("\n These are all the books in our collection. \n")
    books = SHEET.worksheet('Books').get('A:C')

    sleep(1.3)
    print(tabulate(books, headers="firstrow", tablefmt="presto",
          maxcolwidths=[None, 23]))

    checkout()


def main():
    '''
    Starting point of the program. Calls multiple functions.
    '''
    introduction()
    user = user_input()
    purpose(user)


main()
