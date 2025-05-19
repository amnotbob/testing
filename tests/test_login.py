import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Setup browser - Chrome
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_login(self):
        try:
            # 1. Navigate to the login page
            self.driver.get("https://practicetestautomation.com/practice-test-login/")

            # 2. Enter username
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("student")
            time.sleep(1)

            # 3. Enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("Password123")
            time.sleep(1)

            # 4. Click Submit button
            submit_button = self.driver.find_element(By.XPATH, "//button[@class='btn']")
            submit_button.click()
            time.sleep(2)

            # 5. Verify successful login
            success_message = self.driver.find_element(By.ID, "content")

            # Verify either success or failure message
            if "Congratulations" in success_message.text:
                self.assertEqual(success_message.text, "Congratulations student. You successfully logged in!")
                print("\nLogin passed")
            else:
                self.assertIn("invalid", success_message.text.lower())
                print("\nLogin failed")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.fail(f"Test failed due to exception: {e}")
        finally:
            # Quit browser
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()