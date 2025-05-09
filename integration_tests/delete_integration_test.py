import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ToDoAppDeleteTaskTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000/register")
        time.sleep(1)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_delete_task(self):
        driver = self.driver
        username = f"user{int(time.time())}"
        password = "test123"
        task_content = "task to delete"

        # Rejestracja
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(5)

        # Logowanie
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(5)

        # Dodanie zadania
        driver.find_element(By.NAME, "content").send_keys(task_content)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(5)
        self.assertIn(task_content, driver.page_source)

        # Usuwanie zadania (pierwszy przycisk delete)
        delete_forms = driver.find_elements(By.XPATH, "//form[contains(@action, '/task/delete')]")
        self.assertGreater(len(delete_forms), 0, "Nie znaleziono formularza usuwania zadania")
        delete_forms[0].submit()
        time.sleep(5)

        # Wylogowanie
        driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(1)

        # Ponowne logowanie
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.TAG_NAME, "form").submit()
        time.sleep(1)

        # Sprawdzenie, czy zadania nie ma
        self.assertNotIn(task_content, driver.page_source)

if __name__ == "__main__":
    unittest.main()
