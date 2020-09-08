from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys
import requests

# Upplösningar som selenium ska ta screenshots av
resolutions = [[1024, 768],
               [1280, 800],
               [1366, 768],
               [1920, 1080],
               [2560, 1440],
               [3840, 2160]]

# Startar chrome "headless", alltså att webbläsar-rutan inte syns
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Kollar om argumentet "online" skickades med, i vilket fall hemsidan på nätet testas. Annars testas den lokala filen.
    if len(sys.argv) > 1 and sys.argv[1] == "online":
        page = "https://fabilus.gitlab.io/frisorhemsida"

        req = requests.get(page)
        req.close()

        # Kollar om hemsidan inte går att hitta online, ändrar strängen Exception om detta är fallet
        if req.status_code != requests.codes['ok']:
            raise Exception("Statuskod: " + str(req.status_code) +
                            "\nLänk: " + page)

    else:
        # Kollar om filen existerar
        page = "{}/public/index.html".format(os.getcwd())
        if not os.path.exists(page):
            raise Exception("Kan inte hitta filen: " + page)

    driver.get(page)

    # Skapar en mapp för screenshots ifall den inte existerar
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")

    # Tar screenshots i alla specifierade upplösningar och spara resultaten som "BreddxHöjd.png" i screenshots
    for (width, height) in resolutions:
        driver.set_window_size(width, height)
        driver.save_screenshot("screenshots/{}x{}.png".format(width, height))

# Skriver ut error-meddelanden ifall de uppstår
except Exception as err:
    print("ERROR:\n" + str(err), file=sys.stderr)


# Avslutar chrome
driver.quit()
