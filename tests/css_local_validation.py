# Imports the necessary selenium extensions
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Locates the parent directory of tests aka "frisorhemsida"
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Where we want to go from the parent directory => index
desiredPath = "\\public\\css\style.css"

# Creates a variable "options" with the Options() class attributes
options = Options()

# Sets the headless option to True (Runs without a window (Set to: Failure to see live))
options.headless = True

# Variable with location to chromedriver.exe and the headless option
driver = webdriver.Chrome(options=options)


# Validates Locally

# ==========================================================================================================

# Loads in the website
driver.get("https://jigsaw.w3.org/css-validator/#validate_by_upload")

# Looks for the id "file" element and sends the file path to index aka PATH2
driver.find_element_by_id("file").send_keys(parentPath + desiredPath)

# Looks for the specific "xpath" aka the "Granska" button and clicks it
driver.find_element_by_xpath("/html/body/div[2]/div/fieldset[2]/form/p[3]/label/a").click()

print("Validating locally...")
# If
try:
    driver.find_element_by_id("congrats")
    print("Success! The local CSS code is validated.\n")
#Else
except:
    print("Failure! The local CSS code i NOT validated.\n Errors:\n")
    # Looks in the "errors" tag and prints out the content aka the errors
    print("ERRORS:")
    print("=============================================================")

    # Looks in the "errors" tag and prints out the content aka the errors
    for mistakes in driver.find_elements_by_id("errors"):
       print(mistakes.text, "\n")
    # Looks in the "warnings" tag and prints out the content aka the errors
    print("WARNINGS:")
    print("=============================================================")
    # Looks in the "warnings" tag and prints out the content aka the errors
    for warnings in driver.find_elements_by_id("warnings"):
        print(warnings.text, "\n")