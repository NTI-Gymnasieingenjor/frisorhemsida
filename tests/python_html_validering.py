import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    # Testet startar
    def test_search_in_python_org(self):
        driver = self.driver

        # Laddar in hemsidan
        driver.get("https://validator.w3.org")
        elem = driver.find_element_by_name("uri")
        elem.send_keys("https://fabilus.gitlab.io/frisorhemsida/")
        elem.send_keys(Keys.RETURN)

        # Laddar in nya element
        driver.get("https://validator.w3.org/nu/?doc=https%3A%2F%2Ffabilus.gitlab.io%2Ffrisorhemsida%2F")

        # Försöker hitta classen success
            # Om den inte hittar success på sidan så har den misslyckat valideringen
        verify = driver.find_element_by_class_name("success")

        assert "No results found." not in driver.page_source

if __name__ == "__main__":
    unittest.main()