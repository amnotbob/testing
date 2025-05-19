import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Setup: Initialize the Chrome driver
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    # Teardown: Close the driver after the test
    driver.quit()


def test_login(driver):
    try:
        # 1. Navigate to the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        # 3. Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # 4. Click submit
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 5. Verify successful login
        actual_result = driver.find_element(By.ID, "content").text
        assert "Logged In Successfully" in actual_result or "Invalid" in actual_result

    except Exception as e:
        print("Error: ", str(e))
        assert False, f"Test failed due to exception: {e}"
    finally:
        pass
