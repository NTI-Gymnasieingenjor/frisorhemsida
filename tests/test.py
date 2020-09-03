from selenium import webdriver
import time
import os
import sys

driver = webdriver.Chrome()

# Kollar om ett argument har skickats med, i vilket fall hemsidan som ligger uppe testas istället för filerna på datorn
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
