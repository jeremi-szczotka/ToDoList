import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestEmptyTaskAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_empty_task(self):
        driver = self.driver
        driver.get("http://localhost:5000/register")
        time.sleep(1)

        username = f"user{int(time.time())}"
        password = "test123"

     
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

     
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

      
        driver.find_element(By.NAME, "content").send_keys("   ")
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

      
        tasks = driver.find_elements(By.CLASS_NAME, "list-group-item")
       
        self.assertTrue(any("Brak zadań" in t.text for t in tasks))

if __name__ == "__main__":
    unittest.main()