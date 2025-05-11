import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestInvalidLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000/login")
        time.sleep(1)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login_with_wrong_credentials(self):
        driver = self.driver

      
        driver.find_element(By.NAME, "username").send_keys("nieistniejacy_uzytkownik")
        driver.find_element(By.NAME, "password").send_keys("zlehaslo123")
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

        
        self.assertIn("login", driver.current_url)
        self.assertIn("Nie poprawna nazwa użytkownika lub hasło", driver.page_source)

if __name__ == "__main__":
    unittest.main()
