from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

# Kollar om ett argument har skickats med, i vilket fall hemsidan som ligger uppe testas istället för filerna på datorn
# Starta filen i VSCode med F5 (debugging) för att skicka med argumentet "online", använd annars [CTRL + F5] (normal)
if len(sys.argv) > 1:
    page = "https://fabilus.gitlab.io/frisorhemsida"
else:
    page = "file://{}\index.html".format(os.getcwd())

# Testar om filen existerar/hemsidan ligger uppe
try:
    driver.get(page)
except:
    print("Kan inte hitta filen/länken")
    quit()

# Kollar om företagets namn står någonstans på sidan
if "Salong Gloria" not in driver.page_source:
    print("Det finns inget meddelande om att sidan tillhör företaget!")

# Avsluta programmet
driver.quit()
