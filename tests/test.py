from selenium import webdriver
import time

driver = webdriver.Chrome(
    "C:/Users/joakim.kokocha/Documents/chromedriver/chromedriver.exe")

try:
    driver.get("https://fabilus.gitlab.io/frisorhemsida/")
except:
    print("Hemsida inte tillgänglig på internet")


# driver.set_window_size(1920, 1080)
# driver.save_screenshot('screentest.png')

# driver.set_window_size(1120, 1080)
# driver.save_screenshot('screentest2.png')
