import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestDashboardWithoutLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_dashboard_requires_login(self):
        driver = self.driver
        driver.get("http://localhost:5000/dashboard")
        time.sleep(1)

        # Sprawdzenie, czy zostaliśmy przekierowani na stronę logowania
        self.assertIn("login", driver.current_url)

        # Sprawdzenie, czy strona zawiera formularz logowania
        self.assertIn("Login", driver.page_source)  # Nagłówek strony
        self.assertIn("username", driver.page_source.lower())  # Pole loginu (z małej litery)

if __name__ == "__main__":
    unittest.main()
