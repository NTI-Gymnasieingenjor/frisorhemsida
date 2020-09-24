# Imports the important libraries we are using
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Creates a variable "options" with the Options() class attributes
options = Options()
# Sets the headless (Starts a window without ever opening the browser) option to True
options.headless = True

# Variable with PATH and the headless option that later starts a chrome window
driver = webdriver.Chrome(chrome_options=options)

# Locates the parent directory of tests aka "frisorhemsida"
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Where we want to go from the parent directory => index
desiredPath = "\\public\\index.html"

# Loads in the website
driver.get(parentPath+desiredPath)

# Variable which will look for the specified text by id
element = driver.find_element_by_id('title')

# Variable which will look for the specified text ("//*[contains(text(), 'Desired text here')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Tjänster')]")
element = driver.find_element_by_id('table-services')

element = driver.find_element_by_id('smallImages')
element = driver.find_element_by_id('longImage')


element = driver.find_element_by_xpath("//*[contains(text(), 'Kontaktinfo')]")
element = driver.find_element_by_xpath("//*[contains(text(), '0630-555-555')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'info@fabilus.gitlab.io')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Fjällgatan 32H')]")

element = driver.find_element_by_xpath("//*[contains(text(), 'Öppettider')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Mån‑Fre:')]")
element = driver.find_element_by_xpath("//*[contains(text(), '10‑16')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Lördag:')]")
element = driver.find_element_by_xpath("//*[contains(text(), '12‑15')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Söndag:')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Stängt')]")

# Prints out the element that wasn't found on the website
print(element) 
# If all elements are present the code is excellent
print("Code is working excellent")
