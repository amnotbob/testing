import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Setup method to initialize the WebDriver
        try:
            self.driver = webdriver.Chrome()  # Or any other browser you prefer
            self.driver.get("https://practicetestautomation.com/practice-test-login/")
            print("Webpage loaded successfully")
        except Exception as e:
            print("Error during setUp: ", str(e))
            self.fail(f"setUp failed: {e}")

    def test_login_success(self):
        # Test case to check successful login
        try:
            # Locate username field and enter username
            username_field = self.driver.find_element(By.ID, "username")
            username_field.send_keys("student")
            print("Username entered successfully")

            # Locate password field and enter password
            password_field = self.driver.find_element(By.ID, "password")
            password_field.send_keys("Password123")
            print("Password entered successfully")

            # Locate submit button and click
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            print("Submit button clicked successfully")

            # Assert that login was successful based on the presence of success message
            success_message = self.driver.find_element(By.ID, "success")
            self.assertEqual("Logged In Successfully", success_message.text)
            print("Login successful and success message verified")

        except Exception as e:
            print("Error during login test: ", str(e))
            self.fail(f"Login test failed: {e}")

    def tearDown(self):
        # Teardown method to close the WebDriver
        try:
            self.driver.quit()
            print("WebDriver closed successfully")
        except Exception as e:
            print("Error during tearDown: ", str(e))

if __name__ == "__main__":
    unittest.main()