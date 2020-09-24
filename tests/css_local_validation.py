# Imports the necessary selenium extensions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Creates a variable "options" with the Options() class attributes
options = Options()

# Sets the headless option to True (Runs without a window (Set to: Failure to see live))
options.headless = True

# Two variables with diffrent file paths
PATH = "C:\Program Files (x86)\chromedriver.exe"
# NOTE : Switch out your user to your own, do not use "fredrik.nyberg" as a file path on your PC
#        Make sure it's in the correct path
PATH2 = "C:\\Users\\fredrik.nyberg\\Documents\\GitHub\\frisorhemsida\\public\\index.html"

# Variable with location to chromedriver.exe and the headless option
driver = webdriver.Chrome(PATH, options=options)


# Validates Locally

# ==========================================================================================================

# Loads in the website
driver.get("https://jigsaw.w3.org/css-validator/#validate_by_upload")

# Looks for the id "file" element and sends the file path to index aka PATH2
driver.find_element_by_id("file").send_keys(PATH2)

# Looks for the specific "xpath" aka the "Granska" button and clicks it
driver.find_element_by_xpath("/html/body/div[2]/div/fieldset[2]/form/p[3]/label/a").click()

print("Validating locally...")
# If
try:
    driver.find_element_by_class_name("success")
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