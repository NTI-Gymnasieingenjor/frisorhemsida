# Imports the necessary selenium extensions
import os
from selenium import webdriver

# Variable to tell CI/CD to fail a job if validation fails
errorExit = False

# Locates the parent directory of tests aka "frisorhemsida"
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Where we want to go from the parent directory => style.css
desiredPath = "/public/css/style.css"

# Creates a variable "options" with the Options() class attributes
options = webdriver.ChromeOptions()

# Adds the no-sandbox as an argument
options.add_argument("no-sandbox")
# Adds headless as an argument
options.add_argument("headless")

driver = webdriver.Chrome(options=options)


# Validates Locally

# ==========================================================================================================

# Loads in the website
driver.get("https://jigsaw.w3.org/css-validator/#validate_by_upload")

# Looks for the id "file" element and sends the file path to index aka PATH2
driver.find_element_by_id("file").send_keys(parentPath + desiredPath)

# Looks for the specific "xpath" aka the "Granska" button and clicks it
driver.find_element_by_xpath("/html/body/div[2]/div/fieldset[2]/form/p[3]/label/a").click()

print("Validating...")
# If
try:
    driver.find_element_by_id("congrats")
    print("Success! The CSS code is validated.\n")
# Else
except:
    print("Failure! The CSS code is NOT validated.\n")

    # Looks in the "errors" tag and prints out the content aka the errors
    print("ERRORS:")
    print("=============================================================")
    # Looks in the "errors" tag and prints out the content aka the errors
    for mistakes in driver.find_elements_by_id("errors"):
       print(mistakes.text, "\n")

    # Looks in the "warnings" tag and prints out the content aka the warnings
    print("WARNINGS:")
    print("=============================================================")
    # Looks in the "warnings" tag and prints out the content aka the warnings
    for warnings in driver.find_elements_by_id("warnings"):
        print(warnings.text, "\n")
    errorExit = True

if errorExit:
    exit(1)
