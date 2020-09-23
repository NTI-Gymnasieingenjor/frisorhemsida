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

# ==========================================================================================================

# Validates Locally

# ==========================================================================================================

# Loads in the website
driver.get("https://html5.validator.nu/")

# Variable which looks in dropdown menu element "docselect"
select = Select(driver.find_element_by_id("docselect"))
# Looks for element "File Upload" in the visable dropdown menu "docselect"
select.select_by_visible_text("File Upload")

# Looks for the id "doc" element and sends the file path to index aka PATH2
driver.find_element_by_id("doc").send_keys(PATH2)

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

# Validates Online

# ==========================================================================================================

driver.get("https://html5.validator.nu/")

select = Select(driver.find_element_by_id("docselect"))
select.select_by_visible_text("Address")

# Looks for the id "doc" element and sends URL of our website
driver.find_element_by_id("doc").send_keys("https://fabilus.gitlab.io/frisorhemsida/")

link = driver.find_element_by_id('submit')
link.click()

print("Validating online...")
try:
    driver.find_element_by_class_name("success")
    print("Success! The online code is validated.\n")
except:
    print("Failure! The online code i NOT validated.\n")
    for mistakes in driver.find_elements_by_tag_name('ol'):
       print(mistakes.text)
       print("\n")