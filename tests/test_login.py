import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Setup: Initialize WebDriver
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    # Teardown: Close WebDriver after test
    driver.quit()


def test_login(driver):
    # Test case: Login to the practice website
    try:
        # 1. Navigate to the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Enter username and password
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys("student")
        password_field.send_keys("Password123")

        # 3. Click the login button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Verify successful login
        success_message = driver.find_element(By.ID, "content")
        assert "Logged In Successfully" in success_message.text

    except Exception as e:
        print("Error: ", str(e))
        raise e # Re-raise the exception to mark the test as failed.
    finally:
        print("Test Completed")
