# Imports the important libraries we are using
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Creates a variable "options" with the Options() class attributes
options = Options()
# Sets the headless (Starts a window without ever opening the browser) option to True
options.headless = False

# Makes a variable with the path to the chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Variable with PATH and the headless option that later starts a chrome window
driver = webdriver.Chrome(PATH, chrome_options=options)

# Loads in the website
driver.get("https://validator.w3.org/#validate_by_upload")
