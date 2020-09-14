from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
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
address = "Fjällgatan 32H"
postcode = "981 39 KIRUNA"
opening_hours = [
    "10-16",
    "12-15"
]


def page_source_check(value, message):
    """
    Kollar igenom html-koden för att se om en viss sträng finns i den\n
    Parametrar:\n
        value (str): Strängen som funktionen söker efter
        message (str): Errormeddelande

    Returnerar:\n
        Eventuellt errormeddelande
    """
    if value not in driver.page_source:
        return message + "\n"
    return ""


def link_check(link_text, valid_link, message):
    """
    Kollar om en länk finns på sidan och är giltig\n
    Parametrar:\n
        link_text (str): Hyperlink-texten
        valid_link (str): Den "riktiga" länk-texten
        message (str): Errormeddelande

    Returnerar:\n
        Eventuellt errormeddelande
    """
    try:
        elem = driver.find_element_by_link_text(link_text)

        if elem.get_attribute("href") != valid_link:
            return message + "\n"

    except NoSuchElementException:
        return "Inget element med texten \"{}\" existerar\n".format(link_text)
    except Exception as e:
        return e
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
    errors += page_source_check(mail, "E-postadress saknas.")

    # Kollar om butikens gatuadress finns på hemsidan
    errors += page_source_check(address, "Adress saknas.")

    # kollar om butikens postnummer finns på hemsidan
    errors += page_source_check(postcode, "Postnummer saknas.")

    # Kollar om butikens öppettider finns på hemsidan
    for hours in opening_hours:
        errors += page_source_check(hours,
                                    "Öppettiden {} saknas.".format(hours))

    # Väntar i 3 sekunder för att animationen ska bli klar
    driver.implicitly_wait(3)

    # Kollar om butikens e-postadress är korrekt
    errors += link_check(mail, "mailto:" + mail,
                         "Giltig länk till e-post saknas.")

    # Kollar om butikens telefonnummer är korrekt
    errors += link_check(phone, "tel:" + phone.replace("-", ""),
                         "Giltig länk till telefonnummer saknas.")

    if errors != "":
        raise Exception(errors)

    print("Koden klarar alla tester :)")

# Skriver ut error-meddelanden ifall de uppstår
except Exception as err:
    print("ERROR:\n" + str(err), file=sys.stderr)

# Avslutar chrome
driver.quit()
