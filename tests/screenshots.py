from selenium import webdriver
import os
import sys

driver = webdriver.Chrome()

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

# Upplösningar som programmet ska ta screenshots av
resolutions = [[1024, 768],
               [1280, 800],
               [1366, 768],
               [1920, 1080],
               [2560, 1440]]

# Skapar en mapp för screenshots ifall den inte existerar
if not os.path.exists("screenshots"):
    os.mkdir("screenshots")

# Ta screenshots i alla specifierade upplösningar och spara resultaten som "BreddxHöjd.png" i screenshots
for (width, height) in resolutions:
    driver.set_window_size(width, height)
    driver.save_screenshot("screenshots/{}x{}.png".format(width, height))

# Avsluta programmet
driver.quit()
