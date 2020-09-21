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
        driver.get("https://pontusgranath.gitlab.io/projekt-spa/")

        import re
        src = driver.page_source

        def checkExists(word):
            x = re.search(word, src)
            self.assertNotEqual(x, None)

        checkExists(r'Välkommen till Stillhetens spa')
        checkExists(r'images/Bild_Massage.jpg')
        checkExists(r'Öppettider')

        checkExists(r'Mån‑Fre:')
        checkExists(r'Lör:')
        checkExists(r'Sön:')

        checkExists(r'10‑16')
        checkExists(r'12‑15')
        checkExists(r'Stängt')

        checkExists(r'Tjänster')
        checkExists(r'Pris')

        checkExists(r'Helkroppsmassage')
        checkExists(r'Halvkroppsmassage')
        checkExists(r'Halvkroppsmassage')
        checkExists(r'Student helkroppsmassage')
        checkExists(r'Helkroppsmassage stamkund')
        checkExists(r'Sjukgymnast rehab')

        checkExists(r'300&nbsp;kr')
        checkExists(r'450&nbsp;kr')
        checkExists(r'600&nbsp;kr')
        checkExists(r'300&nbsp;kr')
        checkExists(r'400&nbsp;kr')
        checkExists(r'450&nbsp;kr')
        checkExists(r'500&nbsp;kr')
        checkExists(r'800&nbsp;kr')

        checkExists(r'Fjällgatan 32H')
        checkExists(r'981&nbsp;39&nbsp;KIRUNA')
        checkExists(r'0630‑555‑555')
        checkExists(r'info@pontusgranath.gitlab.io')

        checkExists(r'images/Bild_Stenar.jpg')
        checkExists(r'images/Bild_Ljus.jpg')
        checkExists(r'images/Bild_Massage.jpg')

        checkExists(r'images/Bild_Stenar.jpg')
        checkExists(r'images/Bild_Ljus.jpg')
        checkExists(r'images/Bild_Massage.jpg')

        checkExists(r'https://facebook.com/ntiuppsala')
        checkExists(r'https://twitter.com/ntiuppsala')
        checkExists(r'https://instagram.com/ntiuppsala')

if __name__ == "__main__":
    unittest.main()
