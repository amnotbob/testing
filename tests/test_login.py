import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Setup
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()


def test_login_success(driver):
    # 1. Navigate to the login page
    try:
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
        assert success_message.is_displayed()
        assert "Logged In Successfully" in success_message.text

    except Exception as e:
        print("Error: ", str(e))
    finally:
        pass


def test_login_failure(driver):
    # 1. Navigate to the login page
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Enter invalid username and password
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys("invalidUser")
        password_field.send_keys("invalidPassword")

        # 3. Click the login button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Verify login failure message
        error_message = driver.find_element(By.ID, "error")
        assert error_message.is_displayed()
        assert "Your username is invalid!" in error_message.text

    except Exception as e:
        print("Error: ", str(e))
    finally:
        pass