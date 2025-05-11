import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class ToDoAppIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  
        self.driver.get("http://localhost:5000/register")
        time.sleep(10)  
        self.driver.maximize_window()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration_and_login(self):
        driver = self.driver
        username = f"user{int(time.time())}"
        password = "test123"

        
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(10)

      
        assert "login" in driver.current_url


        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(10)

       
        self.assertIn("dashboard", driver.current_url)
        self.assertTrue("Add" in driver.page_source or "Logout" in driver.page_source)
    
    
if __name__ == "__main__":
    unittest.main()
