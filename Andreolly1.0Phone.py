def logo():
    print("!-----------------------------------!")
    print("!-----------------------------------!")
    print("!--------- ANDR3OLLY'S 1.0 ---------!")
    print("!-----------------------------------!")
    print("!-----------------------------------!")

    print("\n ANDR3OLLY - Developed by @Andr3olly")





# ---! Made by @Andr3olly !--- #

import time
import requests
import os
import string
import random
from colorama import Fore

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
            exit()
        elif scelta == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            Conversione_valuta()
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



def Conversione_valuta():
    print("---! WELCOME TO THE CURRENCY CONVERTER !---")

    api_key = "8bcad38b9df668aee6452400405744ad"
    url = "http://apilayer.net/api/live"
    
    importo = float(input("\n Enter the amount: "))
    from_currency = input("\n Write the starting currency (ex. EUR): ").upper()
    to_currency = input("\n Write the final currency (ex. USD): ").upper()

    params = {
        'access_key': api_key,
        'currencies': f'{to_currency},{from_currency}',
        'source': 'USD',
        'format': 1
    }

    response = requests.get(url, params=params)
    json_data = response.json()

    
    if from_currency == "USD":
        rate = json_data['quotes'][f'USD{to_currency}']
        result = importo * rate
    elif to_currency == "USD":
        rate = json_data['quotes'][f'USD{from_currency}']
        result = importo / rate
    else:
        rate_from_usd = json_data['quotes'][f'USD{from_currency}']
        rate_to_usd = json_data['quotes'][f'USD{to_currency}']
        amount_in_usd = importo / rate_from_usd
        result = amount_in_usd * rate_to_usd

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


    domanda_di_continuo = input("\n Do you want to continue with the program? y/n ")

    if domanda_di_continuo == "N" or domanda_di_continuo == "n":
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menù()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    

    peso = float(input("\n Enter your weight in kg: "))
    altezza = float(input("\n Enter your height in cm: "))
    altezza = altezza/100
    imc = peso/(altezza**2)
    print("\n Your BMI is: {:2f}".format(imc))

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

    length = int(input("\n Enter the password length: "))

    if length == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        menù()

    password = []

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



def Meteo():
    print("\n ---! WELCOME TO WEATHER FORECAST !---")

    posizione = input("\n Enter your location: ")

    base_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{posizione}/?key=BE6LBMPRFCNZMSM9842G94J3K"

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