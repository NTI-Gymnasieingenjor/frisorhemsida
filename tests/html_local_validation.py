# Imports the necessary selenium extensions
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Locates the parent directory of tests aka "frisorhemsida"
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))



# Where we want to go from the parent directory => index
desiredPath = "\\public\\index.html"

chromePath = os.getcwd()
chromePath2 = "/chromedriver.exe"

PATH = chromePath + chromePath2

print(chromePath)


# Creates a variable "options" with the Options() class attributes
options = Options()

# Sets the headless option to True (Runs without a window (Set to: Failure to see live))
options.headless = True

# Variable with location to chromedriver.exe and the headless option
driver = webdriver.Chrome(executable_path=PATH, options=options)


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

print("Validating locally...")
# If
try:
    driver.find_element_by_class_name("success")
    print("Success! The local code is validated.\n")
#Else
except:
    print("Failure! The local code i NOT validated.\n Errors:\n")
    # Looks in the "ol" tag and prints out the content aka the errors
    for mistakes in driver.find_elements_by_tag_name('ol'):
       print(mistakes.text, "\n")

# ==========================================================================================================
