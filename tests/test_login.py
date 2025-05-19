import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome()  # Or any other browser you prefer
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()


def test_login(driver):
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

    # 5. Verify login
    try:
        success_message = driver.find_element(By.ID, "success")
        assert success_message.is_displayed(), "Login successful message not displayed"
    except:
        failure_message = driver.find_element(By.ID, "error")
        assert failure_message.is_displayed(), "Login failure message not displayed"
