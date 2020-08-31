from selenium import webdriver
import time
import os

driver = webdriver.Chrome()


# Testar om hemsidan är tillgänglig från internet
try:
    driver.get("https://fabilus.gitlab.io/frisorhemsida/")
except:
    print("Hemsida inte tillgänglig på internet")


# Tar screenshots på hemsidan i olika upplösningar
resolutions = [[1024, 768], [1280, 800], [
    1366, 768], [1920, 1080], [2560, 1440]]

if not os.path.exists("screenshots"):
    os.mkdir("screenshots")

for (w, h) in resolutions:

    driver.set_window_size(w, h)
    driver.save_screenshot("screenshots/{}x{}.png".format(w, h))

driver.quit()

# driver.set_window_size(1920, 1080)
# driver.save_screenshot('screentest.png')

# driver.set_window_size(1120, 1080)
# driver.save_screenshot('screentest2.png')
