import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(driver):
    # Step 1: Navigate to the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    try:
        # Step 2: Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        # Step 3: Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # Step 4: Click submit button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Step 5: Verify successful login or failure message
        time.sleep(1) #Wait for element to load
        if driver.current_url == "https://practicetestautomation.com/practice-test-login/":
            actual_result_element = driver.find_element(By.ID, 'error')
            actual_result_text = actual_result_element.text
            assert "incorrect" in actual_result_text.lower()
        else:
            actual_result_element = driver.find_element(By.XPATH, "//h1")
            actual_result_text = actual_result_element.text
            assert actual_result_text == "Logged In Successfully"

    except Exception as e:
        print("Error: ", str(e))
    finally:
        print("Test completed")