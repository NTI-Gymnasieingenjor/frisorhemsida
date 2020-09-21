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
        driver.get("https://fabilus.gitlab.io/frisorhemsida/")

        import re
        src = driver.page_source

        def checkExists(word):
            x = re.search(word, src)
            self.assertNotEqual(x, None)

        checkExists(r'Välkommen till Stillhetens spa')
        checkExists(r'images/Bild_Massage.jpg')
        checkExists(r'Öppettider')

if __name__ == "__main__":
    unittest.main()
