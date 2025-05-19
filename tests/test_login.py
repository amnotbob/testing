import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome WebDriver
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()

    def test_login(self):
        try:
            # 1. Navigate to the login page
            self.driver.get("https://practicetestautomation.com/practice-test-login/")

            # 2. Enter username
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("student")

            # 3. Enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("Password123")

            # 4. Click submit button
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()

            # 5. Verify successful login
            success_message = self.driver.find_element(By.ID, "content")
            actual_message = success_message.text
            self.assertIn("Logged In Successfully", actual_message)

        except Exception as e:
            print("Error: ", str(e))
            self.fail(f"Test failed due to exception: {e}")

        finally:
            # Teardown
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()