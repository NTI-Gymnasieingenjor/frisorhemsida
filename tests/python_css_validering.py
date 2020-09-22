import unittest
from selenium import webdriver
browser = webdriver.Firefox()
from selenium.webdriver.common.keys import Keys
# from pygeckodriver import geckodriver_path

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    # Testet startar
    def test_search_in_python_org(self):
        driver = self.driver

        # Laddar in hemsidan
        driver.get("https://jigsaw.w3.org/css-validator/")
        elem = driver.find_element_by_name("uri")
        elem.send_keys("https://fabilus.gitlab.io/frisorhemsida/")
        elem.send_keys(Keys.RETURN)

        # Laddar in nya element
        driver.get("https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Ffabilus.gitlab.io%2Ffrisorhemsida%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=sv")

        # Försöker hitta classen congrats
            # Om den inte hittar congrats på sidan så har den misslyckat valideringen
        driver.find_element_by_id("congrats")

        assert "No results found." not in driver.page_source


if __name__ == "__main__":
    unittest.main()