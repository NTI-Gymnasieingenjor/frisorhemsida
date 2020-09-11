from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
import requests

# Startar chrome "headless", alltså att webbläsar-rutan inte syns
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

name = "Salong Gloria"
phone = "0630-555-555"
mail = "info@fabilus.gitlab.io"
address = "Fjällgatan 32H 981 39 KIRUNA"
opening_hours = [
    "10-16",
    "12-15"
]


def page_source_check(value, message):
    """
    Kollar igenom html-koden för att se om en viss sträng finns i den

    Parametrar:\n
        value (str): Strängen som funktionen söker efter
        message (str): Errormeddelande

    Returnerar:\n
        Errormeddelandet om strängen inte hittades.
        Annars skickas en tom sträng tillbaka.

    """
    if value not in driver.page_source:
        return message + "\n"
    return ""


try:
    # Kollar om argumentet "online" skickades med, i vilket fall hemsidan på nätet testas. Annars testas den lokala filen.
    if len(sys.argv) > 1 and sys.argv[1] == "online":
        page = "https://fabilus.gitlab.io/frisorhemsida"

        req = requests.get(page)
        req.close()

        # Kollar om hemsidan går att komma åt utan några problem
        if req.status_code != requests.codes['ok']:
            raise Exception("Statuskod: " + str(req.status_code) +
                            "\nLänk: " + page)

    else:
        # Kollar om filen existerar
        page = "{}/public/index.html".format(os.getcwd())
        if not os.path.exists(page):
            raise Exception("Kan inte hitta filen: " + page)

    driver.get(page)

    errors = ""

    # Kollar om företagets namn finns på sidan
    errors += page_source_check(name,
                                "Det finns inget meddelande om att sidan tillhör företaget.")

    # Kollar om företagets telefonnummer finns på hemsidan
    errors += page_source_check(phone, "Telefonnummer till företaget saknas.")

    # Kollar om företagets mail finns på hemsidan
    errors += page_source_check(mail, "Företagsmail saknas.")

    # Kollar om butikens gatuadress finns på hemsidan
    errors += page_source_check(address, "Adress saknas.")

    # Kollar om butikens öppettider finns på hemsidan
    for hours in opening_hours:
        errors += page_source_check(hours,
                                    "Öppettiden {} saknas.".format(hours))

    if errors != "":
        raise Exception(errors)

    print("Koden klarar alla tester :)")

# Skriver ut error-meddelanden ifall de uppstår
except Exception as err:
    print("ERROR:\n" + str(err), file=sys.stderr)

# Avslutar chrome
driver.quit()
