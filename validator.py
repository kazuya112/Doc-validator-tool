import re
from rich import print
import pyfiglet

banner = pyfiglet.figlet_format("DOC VALIDATOR")
print(f"[cyan]{banner}[/cyan]")

def aadhaar_validator(number):

    number = number.replace(" ", "")

    pattern = r"^[2-9]{1}[0-9]{11}$"

    if re.match(pattern, number):
        masked = "XXXX XXXX " + number[-4:]
        print(f"[green]Valid Aadhaar[/green] : {masked}")
    else:
        print("[red]Invalid Aadhaar Number[/red]")


def pan_validator(number):

    pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"

    if re.match(pattern, number):
        print(f"[green]Valid PAN Card[/green] : {number}")
    else:
        print("[red]Invalid PAN Number[/red]")


def voter_validator(number):

    pattern = r"^[A-Z]{3}[0-9]{7}$"

    if re.match(pattern, number):
        print(f"[green]Valid Voter ID[/green] : {number}")
    else:
        print("[red]Invalid Voter ID[/red]")


def passport_validator(number):

    pattern = r"^[A-Z]{1}[0-9]{7}$"

    if re.match(pattern, number):
        print(f"[green]Valid Passport Number[/green] : {number}")
    else:
        print("[red]Invalid Passport Number[/red]")


def gst_validator(number):

    pattern = r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$"

    if re.match(pattern, number):
        print(f"[green]Valid GST Number[/green] : {number}")
    else:
        print("[red]Invalid GST Number[/red]")


def dl_validator(number):

    pattern = r"^[A-Z]{2}[0-9]{2}[0-9]{11}$"

    if re.match(pattern, number):
        print(f"[green]Valid Driving Licence[/green] : {number}")
    else:
        print("[red]Invalid Driving Licence Number[/red]")


while True:

    print("""
[1] Aadhaar Validator
[2] PAN Validator
[3] Voter ID Validator
[4] Passport Validator
[5] GST Validator
[6] Driving Licence Validator
[7] Exit
""")

    choice = input("Select Option : ")

    if choice == "1":
        num = input("Enter Aadhaar Number : ")
        aadhaar_validator(num)

    elif choice == "2":
        num = input("Enter PAN Number : ").upper()
        pan_validator(num)

    elif choice == "3":
        num = input("Enter Voter ID : ").upper()
        voter_validator(num)

    elif choice == "4":
        num = input("Enter Passport Number : ").upper()
        passport_validator(num)

    elif choice == "5":
        num = input("Enter GST Number : ").upper()
        gst_validator(num)

    elif choice == "6":
        num = input("Enter Driving Licence Number : ").upper()
        dl_validator(num)

    elif choice == "7":
        break

    else:
        print("[red]Invalid Option[/red]")
