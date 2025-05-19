import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Setup:
    print("Setting up the browser...")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    yield driver
    # Teardown:
    print("Tearing down the browser...")
    driver.quit()


def test_login_success(driver):
    # 1. Go to the login page
    print("Navigating to the login page...")
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # 2. Type username and password
    print("Typing username and password...")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("student")
    password_field.send_keys("Password123")

    # 3. Push the submit button
    print("Clicking the login button...")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Verify that the user has logged in successfully
    print("Verifying successful login...")
    welcome_message = driver.find_element(By.XPATH, "//h1[text()='Logged In Successfully']")
    assert welcome_message.is_displayed(), "Welcome message not displayed. Login failed."
    print("Login successful!")


def test_login_failure(driver):
    # 1. Go to the login page
    print("Navigating to the login page...")
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # 2. Type username and password
    print("Typing incorrect username and password...")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("wronguser")
    password_field.send_keys("wrongpassword")

    # 3. Push the submit button
    print("Clicking the login button...")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 4. Verify the error message
    print("Verifying error message...")
    error_message = driver.find_element(By.ID, "error")
    assert error_message.is_displayed(), "Error message not displayed."
    print("Login failed as expected!")


