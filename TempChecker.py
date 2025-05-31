#Web Scraping Tool For Grabbing The Temperature of A Singular Day In Any City of California

import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
init(Fore)

print(Fore.LIGHTBLACK_EX + "  _______                          _____ _               _    ")
print(Fore.LIGHTBLACK_EX + " |__   __|                        / ____| |             | |   ")
print(Fore.LIGHTBLACK_EX + "    | | ___ _ __ ___  _ __ ______| |    | |__   ___  ___| | __")
print(Fore.LIGHTBLACK_EX + "    | |/ _ \ '_ ` _ \| '_ \______| |    | '_ \ / _ \/ __| |/ /")
print(Fore.LIGHTBLACK_EX + "    | |  __/ | | | | | |_) |     | |____| | | |  __/ (__|   < ")
print(Fore.LIGHTBLACK_EX + "    |_|\___|_| |_| |_| .__/       \_____|_| |_|\___|\___|_|\_\ ")
print(Fore.LIGHTBLACK_EX + "                     | |                                      ")
print(Fore.LIGHTBLACK_EX + "                     |_|                                      ")
print(Fore.LIGHTBLACK_EX + "Author: github.com/poefsa")

print("")

userOption = str(input("Please Enter The City You Would Like To Check The Temperature Of: "))
url = f"https://www.wunderground.com/weather/us/ca/{userOption}"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

try: 
    response = requests.get(url, headers=headers)
    response.raise_for_status() 
    
    soup = BeautifulSoup(response.text, 'html.parser')
    userTemp = soup.find('span', class_='wu-value wu-value-to')
    
    if userTemp:
        valueF = userTemp.text
        print(f"It is {Fore.YELLOW}{valueF}°F in {userOption}!")
    else:
        print(Fore.RED + "Sorry, temperature info not found. Check the city name and try again.")

except requests.RequestException as e:
    print(Fore.RED + f"There was an error in fetching the data!: {e}")