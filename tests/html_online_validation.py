# Imports the necessary selenium extensions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# Creates a variable "options" with the Options() class attributes
options = Options()

# Sets the headless option to True (Runs without a window (Set to: Failure to see live))
options.headless = True

# Variable with location to chromedriver.exe and the headless option
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome(ChromeDriverManager().install())


# Validates Online

# ==========================================================================================================

# Loads in the website
driver.get("https://html5.validator.nu/")

# Variable which looks in dropdown menu element "docselect"
select = Select(driver.find_element_by_id("docselect"))
# Looks for element "File Upload" in the visable dropdown menu "docselect"
select.select_by_visible_text("Address")

# Looks for the id "doc" element and sends URL of our website
driver.find_element_by_id("doc").send_keys("https://fabilus.gitlab.io/frisorhemsida/")

# Makes a variable which stores the "submit" element. The check button on the browser
link = driver.find_element_by_id('submit')
# Clicks on the stored element
link.click()

print("Validating online...")
# If
try:
    driver.find_element_by_class_name("success")
    print("Success! The online code is validated.\n")
# Else
except:
    print("Failure! The online code i NOT validated.\n")
    # Looks in the "ol" tag and prints out the content aka the errors
    for mistakes in driver.find_elements_by_tag_name('ol'):
       print(mistakes.text)
       print("\n")

# ==========================================================================================================
