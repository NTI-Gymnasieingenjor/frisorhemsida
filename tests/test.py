from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
import requests

# Startar chrome "headless", alltså att webbläsar-rutan inte syns
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Kollar om ett argumenar skickats med, i vilket fall hemsidan som ligger uppe testas istället för filerna på datorn
    # Starta filen i VSCode F5(debugging) för att skicka med argumentet "online", använd annars[CTRL + F5](normal)
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

    # Kollar om företagets namn står någonstans på sidan
    if "Salong Gloria" not in driver.page_source:
        raise Exception(
            "Det finns inget meddelande om att sidan tillhör företaget!")

# Skriver ut error-meddelanden ifall de uppstår
except Exception as err:
    print("ERROR:\n" + str(err), file=sys.stderr)

# Avslutar chrome
driver.quit()
