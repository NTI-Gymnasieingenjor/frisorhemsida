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

# Variable with location to chromedriver.exe and the headless option
driver = webdriver.Chrome(PATH, options=options)


# Validates Online

# ==========================================================================================================

# Loads in the website
driver.get("https://jigsaw.w3.org/css-validator/#validate_by_uri")

# Looks for the id "uri" element and sends the URL of the website
driver.find_element_by_id("uri").send_keys("https://fabilus.gitlab.io/frisorhemsida/")

# Looks for the specific "xpath" aka the "Granska" button and clicks it
driver.find_element_by_xpath("/html/body/div[2]/div/fieldset[1]/form/p[3]/label/a/span").click()

print("Validating Online...")
# If
try:
    driver.find_element_by_class_name("success")
    print("Success! The online CSS code is validated.\n")
#Else
except:
    print("Failure! The online CSS code i NOT validated.\n Errors:\n")
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