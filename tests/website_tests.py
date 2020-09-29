# Imports the important libraries we are using
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Locates the parent directory of tests aka "frisorhemsida"
parentPath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# Where we want to go from the parent directory => index
desiredPath = "\\public\\index.html"

# Creates a variable "options" with the Options() class attributes
options = webdriver.ChromeOptions()

# Adds the no-sandbox as an argument
options.add_argument("no-sandbox")
# Adds headless as an argument
options.add_argument("headless")

driver = webdriver.Chrome(options=options)

# Loads in the website
driver.get("file:///" + parentPath + desiredPath)

# Variable which will look for the specified text by id
element = driver.find_element_by_id('title')

# Variable which will look for the specified text ("//*[contains(text(), 'Desired text here')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Tjänster')]")
element = driver.find_element_by_id('tableServices')

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
