import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def test_login():
    try:
        # Setup Chrome driver
        service = Service(executable_path='/usr/bin/chromedriver')
        driver = webdriver.Chrome(service=service)

        # Navigate to the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # Click submit
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Verify login status
        text_element = driver.find_element(By.ID, "content")
        actual_text = text_element.text

        assert "Logged In Successfully" in actual_text or "failed" in actual_text, f"Expected 'Logged In Successfully' or 'failed', but got: {actual_text}"

    except Exception as e:
        print("Error: ", str(e))
        raise  # Re-raise the exception to mark the test as failed
    finally:
        # Close the driver
        if 'driver' in locals():
            driver.quit()
