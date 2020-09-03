from selenium import webdriver
import time
import os

driver = webdriver.Chrome()

# Testar om filen existerar
try:
    driver.get("file://{}/index.html".format(os.getcwd()))
except:
    print("Kan inte hitta index.html")
    quit()

# Kollar om företagets namn står någonstans på sidan
if "Salong Gloria" not in driver.page_source:
    print("Det finns inget meddelande om att sidan tillhör företaget!")

# Avsluta programmet
driver.quit()
