import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestMassTaskAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000/register")
        time.sleep(1)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_50_tasks(self):
        driver = self.driver
        username = f"user{int(time.time())}"
        password = "test123"

        # Rejestracja
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

        # Logowanie
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

        # Dodanie 50 zadań
        for i in range(50):
            driver.find_element(By.NAME, "content").send_keys(f"Zadanie #{i+1}")
            driver.find_element(By.TAG_NAME, "form").submit()
            time.sleep(0.1)

        time.sleep(1)

        # Sprawdzenie, czy wszystkie 50 zadań się pojawiło
        tasks = driver.find_elements(By.XPATH, "//ul/li[contains(@class, 'list-group-item')]")
        self.assertEqual(len(tasks), 50, f"Oczekiwano 50 zadań, ale znaleziono {len(tasks)}.")

if __name__ == "__main__":
    unittest.main()
