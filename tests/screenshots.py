from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os
import sys
import requests
import time

# Upplösningar som selenium ska ta screenshots av
resolutions = [[1024, 768],
               [1280, 800],
               [1366, 768],
               [1920, 1080],
               [2560, 1440],
               [3840, 2160]]


# Kollar om argumentet "-firefox" skickats med, i vilket fall firefox används istället för chrome
if "-firefox" in sys.argv:
    firefox_options = FirefoxOptions()
    # Startar webbläsaren "headless", alltså att webbläsar-rutan inte syns
    firefox_options.add_argument("-headless")
    driver = webdriver.Firefox(options=firefox_options)
else:
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)


try:
    # Kollar om argumentet "-online" skickats med, i vilket fall hemsidan på nätet testas. Annars testas den lokala filen.
    if "-online" in sys.argv:
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
        page = "file://" + page

    driver.get(page)

    # Skapar en mapp för screenshots ifall den inte existerar
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")

    # Väntar in hemsidans animationer
    time.sleep(2)

    # Tar screenshots i alla specifierade upplösningar och spara resultaten som "BreddxHöjd.png" i screenshots
    for (width, height) in resolutions:
        # Lagrar differensen mellan fönstrets totala storlek och storleken av fönstrets innehåll i variabler
        dx, dy = driver.execute_script(
            "var w=window; return [w.outerWidth - w.innerWidth, w.outerHeight - w.innerHeight];")
        # Ser till att upplösningen är korrekt genom att addera storleken av webbläsarens border (dx, dy) till width och height
        driver.set_window_size(width + dx, height + dy)
        driver.save_screenshot(
            "screenshots/{}x{}.png".format(width, height))

# Skriver ut error-meddelanden ifall de uppstår
except Exception as err:
    print("ERROR:\n" + str(err), file=sys.stderr)


# Avslutar webbläsaren
driver.quit()
