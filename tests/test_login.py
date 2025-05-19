import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Setup: Launch browser
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    yield driver
    # Teardown: Close browser
    driver.quit()


def test_login_success(driver):
    # 1. Navigate to the login page
    print("Navigating to login page...")
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Login page loaded.")

    # 2. Enter username and password
    print("Entering username and password...")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("student")
    password_field.send_keys("Password123")
    print("Username and password entered.")

    # 3. Click the login button
    print("Clicking login button...")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Login button clicked.")

    # 4. Verify successful login message
    print("Verifying successful login...")
    success_message = driver.find_element(By.ID, "content")
    assert success_message.text == "Logged In Successfully", f"Expected 'Logged In Successfully', but got '{success_message.text}'"
    print("Login successful.")


def test_login_failure(driver):
    # 1. Navigate to the login page
    print("Navigating to login page...")
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Login page loaded.")

    # 2. Enter incorrect username and password
    print("Entering incorrect username and password...")
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("wronguser")
    password_field.send_keys("wrongpassword")
    print("Incorrect username and password entered.")

    # 3. Click the login button
    print("Clicking login button...")
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Login button clicked.")

    # 4. Verify error message
    print("Verifying error message...")
    error_message = driver.find_element(By.ID, "error")
    assert error_message.text == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{error_message.text}'"
    print("Login failed as expected.")


# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])