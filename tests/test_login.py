import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        s = Service('./chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def test_valid_login(self):
        # Enter username
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys("student")
        print("Entered username")

        # Enter password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")
        print("Entered password")

        # Submit the form
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Clicked submit button")

        # Check the confirmation message
        confirmation_element = self.driver.find_element(By.XPATH, "//div[@id='content']//h1")
        confirmation_message = confirmation_element.text
        self.assertEqual(confirmation_message, "Logged In Successfully", "Login failed")
        print("Verified successful login")

    def test_invalid_username(self):
        # Enter invalid username
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys("invalidUser")
        print("Entered invalid username")

        # Enter password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")
        print("Entered password")

        # Submit the form
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Clicked submit button")

        # Check the error message
        error_element = self.driver.find_element(By.ID, "error")
        error_message = error_element.text
        self.assertEqual(error_message, "Your username is invalid!", "Error message is incorrect")
        print("Verified invalid username error")

    def test_invalid_password(self):
        # Enter username
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys("student")
        print("Entered username")

        # Enter invalid password
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("wrongPassword")
        print("Entered invalid password")

        # Submit the form
        submit_button = self.driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Clicked submit button")

        # Check the error message
        error_element = self.driver.find_element(By.ID, "error")
        error_message = error_element.text
        self.assertEqual(error_message, "Your password is invalid!", "Error message is incorrect")
        print("Verified invalid password error")

    def tearDown(self):
        # Close the driver
        self.driver.quit()
        print("Closed the browser")

if __name__ == "__main__":
    unittest.main()