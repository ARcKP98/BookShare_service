
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


def introduction():
    BigBanner = pyfiglet.figlet_format("Bookkeeping service!!")
    print(Fore.YELLOW + Style.BRIGHT + BigBanner)