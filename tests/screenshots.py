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
