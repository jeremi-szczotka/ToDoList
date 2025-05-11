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

        
        self.assertIn("login", driver.current_url)

        self.assertIn("Login", driver.page_source)  
        self.assertIn("username", driver.page_source.lower())  

if __name__ == "__main__":
    unittest.main()
