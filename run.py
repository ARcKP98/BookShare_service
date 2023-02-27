import re
import gspread
import pyfiglet
from colorama import Fore, Style
# import pandas as pd
from tabulate import tabulate
# from pprint import pprint
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


# book = SHEET.worksheet('Biographies')
# data = book.get_all_values()
# data1 = data[1:3]

# pprint(data1)


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


def purpose(name):
    print(f"\n Hi {name}. What would you like to do?")
    print("\n 1. Check out our books. \
        \n 2. Donate a Book.\n")
    while True:
        try:
            choice = int(input("\n Make your choice: "))
            if choice == 1:
                print("\n You would like to see our collection.\n")
                show_books()
                break
            elif choice == 2:
                print("\n You would like to donate a book. How nice!\n")
                donate()
                break
            elif choice:
                print("\n Enter a number from the given options.")
                continue
        except ValueError:
            print("\n Not a number")
            continue


def checkout():
    print("\nIf you would like to borrow a book, enter the checkout code.")
    print("If you don't want to borrow a book and leave this section, press 0.\
        \n")
    decision = input("\n Make a choice: ")
    print(decision)
    pattern = re.compile(r'\b' + decision + r'\b')
    while True:
        try:
            if decision == str(0):
                while True:
                    opt = input("Do you want to leave the " +
                                "program?(Yes/No): ").capitalize()
                    if opt == ('Yes'):
                        print("Leaving the program...")
                        print("\nGoodbye.\n")
                        quit()
                    elif opt == ('No'):
                        print(" \n Taking you back to the genre menu...\n")
                        print("\nWelcome back.\n")
                        show_books()
                        break
                    else:
                        print("Enter a valid input")
                        continue
            else:
                codes = SHEET.worksheet('Books')
                # print("CODES")
                # print(codes)
                code = codes.find(pattern, in_column=1)
                # print("code")
                # print(code)
                # val = code.
                # if decision == code:
                # print(f"This is code.row: {code.row}")
                row_info = codes.row_values(code.row)
                # print(values_list)
                book = row_info[1]
                author = row_info[2]
                print(f"You chose the book {book} by {author}")
                print("Checking out...")
                codes.delete_rows(code.row)
                # Update to other sheets that display? Maybe combine.
                print("Checkout complete.")
                print("Good Bye")
                quit()
                # val = code.row()
                # print(f"You selected the title {val}")
        except AttributeError:
            print("Please enter a number.")
            


def donate():
    don = input("What is the name of the book?(The proper name)\n").title()
    don_reg = re.compile(r'\b' + don + r'\b')
    collection = SHEET.worksheet('Books')
    # print(collection)
    code = collection.find(don_reg, in_column=2)
    print(f"The code is {code}")
    if code is None:
        print("We don't have this book.")
        book = don
        author = input("What is the Author's name?: ")
        chek_code = len(collection.get_all_values())
        # print(chek_code)
        entry = []
        entry.append(chek_code)
        entry.append(book)
        entry.append(author)
        # print(entry)
        print("Adding the entry to the library...")
        collection.append_row(entry)
        print("Thank you for your donation!! Have a nice day.")
    if code:
        row_info = collection.row_values(code.row)
        book = row_info[1]
        print(book)
        print(f"We have {book} in our collection.")
        while True:
            sel = input("\n Would you like to return to main menu?(Y/N): ")
            if sel == 'Y' or sel == 'y':
                print("Returning to main menu.....")
                # Maybe clear screen?
                show_books()
                continue
            elif sel == 'N' or sel == 'n':
                while True:
                    sel = input("Would you like to leave the program?(Y/N): ")
                    if sel == 'Y' or sel == 'y':
                        print("Leaving the program...")
                        print("GoodBye")
                        quit()
                    elif sel == 'N' or sel == 'n':
                        print("Taking you to main menu...")
                        show_books()
                        break


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
                gen1 = SHEET.worksheet('sci-fi').get('A:C')
                # data = pd.DataFrame(gen1)
                # print(data.to_string(index=False, header=False))
                print(tabulate(gen1, headers="firstrow", tablefmt="presto"))
                # gen1 = SHEET.worksheet('sci-fi')
                # # data1 = gen1[1:4]
                # print(gen1)
                break
            if choice == 2:
                print("Loading.......")
                print("\nHere are our biographical titles:\n")
                gen2 = SHEET.worksheet('Biographies').get('A:C')
                # data = pd.DataFrame(gen2)
                # print(data.to_string(index=False, header=False))
                print(tabulate(gen2, headers="firstrow", tablefmt="pretty"))
                break
            if choice == 3:
                print("Loading.......")
                print("\nHere are our Self-Help titles:\n")
                gen3 = SHEET.worksheet('Self-help').get('A:C')
                # data = pd.DataFrame(gen3)
                # print(data.to_string(index=False, header=False))
                print(tabulate(gen3, headers="firstrow", tablefmt="pretty"))

                break
            else:
                print("Please pick from one of the options provided.")
                continue
        except ValueError:
            print("Please enter a number.")
    checkout()


def main():
    introduction()
    user = user_input()
    purpose(user)


main()
