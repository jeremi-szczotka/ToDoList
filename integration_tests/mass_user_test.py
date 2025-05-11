import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegisterMultipleUsers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_register_50_users(self):
        driver = self.driver

        for i in range(50):
            username = f"user_{int(time.time())}_{i}"
            password = "test123"

            driver.get("http://localhost:5000/register")
            time.sleep(0.5)

            driver.find_element(By.NAME, "username").send_keys(username)
            driver.find_element(By.NAME, "password").send_keys(password)
            driver.find_element(By.TAG_NAME, "form").submit()
            time.sleep(0.5)

            
            self.assertIn("login", driver.current_url, f"Rejestracja nie powiodła się dla użytkownika {username}")

if __name__ == "__main__":
    unittest.main()
