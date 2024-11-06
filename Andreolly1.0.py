def logo():
    
    print(figlet_format("ANDR3OLLY'S 1.0", font="standard"))

    print("\n ANDR3OLLY - Developed by @Andr3olly")





# ---! Made by @Andr3olly !--- #

import time
import sys
import requests
import os
from pathlib import Path
import string
import random
import wifi_qrcode_generator.generator
import qrcode
import shutil
from colorama import Fore
from pyfiglet import figlet_format

def caricamento():
    for x in range(0,5):
        b = "\n Loading" + "." *x
        print(b, end="\r")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        
spazio = " " *30
print(spazio, end="\r", flush=True)

time.sleep(2.0)

def del_term():
    os.system('cls' if os.name == 'nt' else 'clear')

 # MENU DELLA SCELTA DEL PROGRAMMA

def menù():
        print("\n 0) TO EXIT \n 1) BMI CALCULATOR \n 2) PASSWORD GENERATOR \n 3) CURRENCY CONVERTER \n 4) QR CODE GENERATOR \n 5) WEATHER FORECAST")
        scelta = input("\n Choose wich option do you wanna use: ")

        

        if scelta == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            IMC()
        elif scelta == "2":
            Password_gen()
        elif scelta == "0":
            print("\n Exiting... ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            sys.exit()
        elif scelta == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            Conversione_valuta()
        elif scelta == "4":
            Qr_code()
            os.system('cls' if os.name == 'nt' else 'clear')
        elif scelta == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            Meteo()
        else:
            print("\n Invalid choice! Returning to the menu...")
            time.sleep(1.0)
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            menù()

        print("\n")


# CONVERTITORE DI VALUTA

def Conversione_valuta():
    print("---! WELCOME TO THE CURRENCY CONVERTER !---")

    api_key = "8bcad38b9df668aee6452400405744ad"
    url = "http://apilayer.net/api/live"
    try:
        importo = float(input("\n Enter the amount: "))
    except ValueError:
        print("\n Import not valid! Please try again..")
        time.sleep(2)
        del_term()
        return Conversione_valuta()
    try:
        from_currency = input("\n Write the starting currency (ex. EUR): ").upper()
        to_currency = input("\n Write the final currency (ex. USD): ").upper()
    except TypeError:
        print("\n Non-existent currency! Please try again..")
        time.sleep(3)
        del_term()
        return Conversione_valuta()

    params = {
        'access_key': api_key,
        'currencies': f'{to_currency},{from_currency}',
        'source': 'USD',
        'format': 1
    }

    response = requests.get(url, params=params)
    json_data = response.json()

    try:
        if from_currency == "USD":
            rate = json_data['quotes'][f'USD{to_currency}']
            result = importo * rate
        if to_currency == "USD":
            rate = json_data['quotes'][f'USD{from_currency}']
            result = importo / rate
        else:
            rate_from_usd = json_data['quotes'][f'USD{from_currency}']
            rate_to_usd = json_data['quotes'][f'USD{to_currency}']
            amount_in_usd = importo / rate_from_usd
            result = amount_in_usd * rate_to_usd
    except (KeyError, TypeError):
        print("\n Currency not valid! Please try again..")
        time.sleep(3)
        del_term()
        return Conversione_valuta()

    print(f"\n The amount of {importo} {from_currency} is equivalent to {result:.2f} {to_currency}.")

    Return = input("\n Do you want to use the program again? y/n:  ")

    if Return == "y" or Return == "Y":
        os.system('cls' if os.name == 'nt' else 'clear')
        Conversione_valuta()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menù()

    


def IMC():
    print("---! WELCOME TO THE BMI CALCULATOR !---")

    try:
        domanda_di_continuo = input("\n Do you want to continue with the program? y/n ")

        if domanda_di_continuo not in ["n", "N", "y", "Y"]:
            print("\n Option not valid! Please try again..")
            time.sleep(2)
            del_term()
            return IMC()

    except ValueError:
        print("\n Option not valid! Please try again..")
        time.sleep(2)
        del_term()
        return IMC()
    if domanda_di_continuo == "N" or domanda_di_continuo == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menù()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    
    try:
        peso = float(input("\n Enter your weight in kg: "))
        altezza = float(input("\n Enter your height in cm: "))
        altezza = altezza/100
        imc = peso/(altezza**2)
        print("\n Your BMI is: {:2f}".format(imc))
    except (ValueError, ZeroDivisionError):
        print("\n Value not valid! Please try again..")
        time.sleep(3)
        del_term()
        return IMC()
    sottopeso = Fore.BLUE
    normopeso = Fore.GREEN
    sovrappeso = Fore.YELLOW
    obeso = Fore.RED

    if imc < 16:
        print("\n VERY UNDERWEIGHT! Eats!")
        print(sottopeso + "-----|Underweight|-----" + Fore.RESET, 
        normopeso + "-----|Normal weight|-----" + Fore.RESET, 
        sovrappeso + "-----|Overweight|-----" + Fore.RESET, 
        obeso + "-----|Obese|-----" + Fore.RESET)
    elif 16 <= imc <= 18.5:
        print("\n Underweight! Eat more!")
        print(sottopeso + "-----|Underweight|-----" + Fore.RESET, 
        normopeso + "-----|NormalWeight|-----" + Fore.RESET, 
        sovrappeso + "-----|Overweight|-----" + Fore.RESET, 
        obeso + "-----|Obese|-----" + Fore.RESET)
    elif 18.5 <= imc <= 25:
        print("\nFantastic! You are NormalWeight!")
        print(sottopeso + "-----|Underweight|-----" + Fore.RESET, 
        normopeso + "-----|NormalWeight|-----" + Fore.RESET, 
        sovrappeso + "-----|Overweight|-----" + Fore.RESET, 
        obeso + "-----|Obese|-----" + Fore.RESET)
    elif 30 <= imc <= 35:
        print("\n Obesity Grade I! Attention...")
        print(sottopeso + "-----|Underweight|-----" + Fore.RESET, 
        normopeso + "-----|Normalweight|-----" + Fore.RESET, 
        sovrappeso + "-----|Overweight|-----" + Fore.RESET, 
        obeso + "-----|Obese|-----" + Fore.RESET)
    elif 35 <= imc <= 40:
        print("\n Obesity Grade II! Try to eat less!!")
        print(sottopeso + "-----|Underweight|-----" + Fore.RESET, 
        normopeso + "-----|Normalweight|-----" + Fore.RESET, 
        sovrappeso + "-----|Overweight|-----" + Fore.RESET, 
        obeso + "-----|Obese|-----" + Fore.RESET)
    elif imc > 40:
        print("\n Obesity Grade III!!! Go to a dietician!")
        print(sottopeso + "-----|Underweight|-----" + Fore.RESET, 
        normopeso + "-----|Normalweight|-----" + Fore.RESET, 
        sovrappeso + "-----|Overweight|-----" + Fore.RESET, 
        obeso + "-----|Obese|-----" + Fore.RESET)
    


    
    ritorno = input("\n Press Enter to return to the menu ")
    os.system('cls' if os.name == 'nt' else 'clear')
    logo()
    menù()

def Password_gen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n ---! WELCOME TO THE PASSWORD GENERATOR !---")
    print("\n 0) TO RETURN TO THE MENU")
    minuscole = string.ascii_lowercase
    maiuscole = string.ascii_uppercase
    numeri = string.digits
    simboli = string.punctuation
    all = minuscole + maiuscole + numeri + simboli
    length = None


    try:
        length = int(input("\n Enter the password length: "))
    except (ValueError, UnboundLocalError):
        print("\n Value not valid! Please try again..")
        time.sleep(3)
        del_term
        return Password_gen()
    if length == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menù()

    password = []
    try:
        for i in range(length):
            randomchar = random.choice(all)
            password.append(randomchar)

        print("\n Your password is: " + "".join(password))

        new_gen = input("\n Do you want to generate another password? y/n: ")

        if new_gen == "n" or new_gen == "N":
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            menù()
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            Password_gen()
    except TypeError:
        del_term()
        return Password_gen()

numero = 1

def Qr_code():
    global numero

    os.system('cls' if os.name == 'nt' else 'clear')
    print("---! WELCOME TO THE QR CODE GENERATOR !---")

    print("\n 0) TO EXIT \n 1) QR CODE FOR WIFI \n 2) SIMPLE QR CODE")

    try:
        scelta = int(input("\n Choose option: "))

        if scelta not in [0,1,2]:
            print("Option not valid please try again..")
            time.sleep(2)
            del_term()
            return Qr_code()

    except (ValueError) as e:
        print(f"\n Error: {e}! Try again..")
        time.sleep(3)
        del_term()
        return Qr_code()


    if scelta == 1:
            try:
                qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
                ssid=input("\n Enter the WiFi SSID: "), hidden=input("\n Is the WiFi hidden? True/False: "), authentication_type=input("\n Enter the type of authentication e.g. WPA/WPA2: "), password=input("\n Enter your wifi password: ")
        )
            except ValueError as e:
                print(f"\n Error: {e}, please try again! " )
                time.sleep(3)
                del_term()
                return Qr_code()
            qr_code.print_ascii()
            file = qr_code.make_image().save(f'qr_code_wifi{numero}.png')

            shutil.move(file, Path.home() / "Desktop")

            numero += 1

    elif scelta == 2:
            contenuto = input("\n Choose what to connect the QR code to e.g. https://google.com: ")
            img = qrcode.make(contenuto)


            desktop_dir = Path.home() / "Desktop"

            if not desktop_dir.exists():
                desktop_dir = Path.home() / "Scrivania"

            file_name = f"qr_code{numero}.png"
            file_path = desktop_dir /file_name

            img.save(file_path)

            print("\n QR Code Generated on Desktop Successfully!")

            numero += 1

    elif scelta == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            menù()

    


    domanda = input("\n Do you want to generate another QR code? y/n: ")


    if domanda == "y" or domanda == "Y":
        del_term()
        return Qr_code()



    if domanda == "n" or domanda == "N":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menù()
    
            

def Meteo():
    print("\n ---! WELCOME TO WEATHER FORECAST !---")

    posizione = input("\n Enter your location: ")
    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{posizione}/?key=BE6LBMPRFCNZMSM9842G94J3K"

    try:
        response = requests.get(base_url)
        response.raise_for_status()

        data = response.json()
    except requests.exceptions.HTTPError:
        print("\n The city does NOT exist! Try again.")
        time.sleep(3)
        del_term()
        return Meteo()
    response = requests.get(base_url)
    response.raise_for_status()
    json_data = response.json()

    if "currentConditions" in json_data:
        condizioni_attuali = json_data["currentConditions"]
        temperatura = condizioni_attuali["temp"]
        descrizione = condizioni_attuali["conditions"]
        umidita = condizioni_attuali["humidity"]
        tempe_celsius = (temperatura - 32) / 1.8

        temperatura_intera = int(tempe_celsius)

        print(f"\n Current weather in {posizione.capitalize()}: ")
        print(f"\n Temperature: {temperatura_intera}°C ")
        print(f"\n Description: {descrizione} ")
        print(f"\n Humidity: {umidita}% ")

    domanda = input("\n Want to see another location? y/n: ")

    if domanda == "Y" or domanda == "y":
        os.system('cls' if os.name == 'nt' else 'clear')
        Meteo()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menù()

caricamento()
menù()