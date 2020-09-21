# Imports the important libraries we are using
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Creates a variable "options" with the Options() class attributes
options = Options()
# Sets the headless (Starts a window without ever opening the browser) option to True
options.headless = True

# Makes a variable with the path to the chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Variable with PATH and the headless option that later starts a chrome window
driver = webdriver.Chrome(PATH, chrome_options=options)

# Loads in the website
driver.get("https://fabilus.gitlab.io/frisorhemsida/")
# Variable which will look for the specified text ("//*[contains(text(), 'Desired text here')]")
element = driver.find_element_by_xpath("//*[contains(text(), 'Öppettider')]")

element = driver.find_element_by_xpath("//*[contains(text(), 'Måndag - Fredag:')]")
element = driver.find_element_by_xpath("//*[contains(text(), '10-16')]")

# Prints out the element that wasn't found on the website
print(element) 
# If all elements are present the code is excellent
print("Code is working excellent")
