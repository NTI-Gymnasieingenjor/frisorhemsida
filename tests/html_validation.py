# Imports the necessary selenium extensions
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Variable to tell CI/CD to fail a job if validation fails
errorExit = False

# Locates the parent directory of tests aka "frisorhemsida"
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Where we want to go from the parent directory => index
desiredPath = "/public/index.html"


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
driver.get("https://html5.validator.nu/")

# Variable which looks in dropdown menu element "docselect"
select = Select(driver.find_element_by_id("docselect"))
# Looks for element "File Upload" in the visable dropdown menu "docselect"
select.select_by_visible_text("File Upload")

# Looks for the id "doc" element and sends the file path to index aka PATH2
driver.find_element_by_id("doc").send_keys(parentPath + desiredPath)

# Makes a variable which stores the "submit" element. The check button on the browser
link = driver.find_element_by_id('submit')
# Clicks on the stored element
link.click()

print("Validating...")
# If
try:
    driver.find_element_by_class_name("success")
    print("Success! The code is validated.\n")
# Else
except:
    print("Failure! The code i NOT validated.\n Errors:\n")
    # Looks in the "ol" tag and prints out the content aka the errors
    for mistakes in driver.find_elements_by_tag_name('ol'):
       print(mistakes.text, "\n")
    errorExit = True

if errorExit:
    exit(1)

# ==========================================================================================================
