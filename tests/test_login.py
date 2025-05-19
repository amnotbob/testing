import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Webpage loaded successfully")
    yield driver
    # Teardown
    driver.quit()
    print("Browser closed")


def test_successful_login(driver):
    # Enter username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")
    print("Username entered")

    # Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    print("Password entered")

    # Click login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Login button clicked")

    # Verify successful login message
    success_message = driver.find_element(By.XPATH, "//h1[text()='Logged In Successfully']")
    assert success_message.is_displayed(), "Success message not displayed"
    print("Login successful")


def test_failed_login(driver):
    # Enter invalid username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("invalidUser")
    print("Invalid username entered")

    # Enter invalid password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("invalidPassword")
    print("Invalid password entered")

    # Click login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Login button clicked")

    # Verify error message
    error_message = driver.find_element(By.ID, "error")
    assert error_message.is_displayed(), "Error message not displayed"
    print("Login failed as expected")
