import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService


# Define test function
def test_login():
    # Setup: Initialize the Chrome webdriver
    try:
        print("Setting up the webdriver...")
        service = ChromeService(executable_path='chromedriver')
        driver = webdriver.Chrome(service=service)
        print("Webdriver initialized successfully.")

        # 1. Navigate to the login page
        print("Navigating to the login page...")
        driver.get("https://practicetestautomation.com/practice-test-login/")
        print("Login page loaded.")

        # 2. Enter username and password
        print("Entering username and password...")
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys("student")
        password_field.send_keys("Password123")
        print("Username and password entered.")

        # 3. Click the submit button
        print("Clicking the submit button...")
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()
        print("Submit button clicked.")

        # 4. Verify successful login
        print("Verifying successful login...")
        logout_button = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button.is_displayed(), "Logout button not found. Login failed."
        print("Logout button found. Login successful.")

        success_message = driver.find_element(By.ID, "content")
        assert success_message.is_displayed(), "Success message is not displayed."
        print("Success message is displayed.")

        assert success_message.text == "Logged In Successfully", "Incorrect success message."
        print("Success message verified.")

    except Exception as e:
        print("Error: ", str(e))
        pytest.fail(f"Test failed due to exception: {str(e)}")
    finally:
        # Teardown: Close the browser
        print("Closing the browser...")
        driver.quit()
        print("Browser closed.")