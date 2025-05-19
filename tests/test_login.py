import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Define test parameters
URL = "https://practicetestautomation.com/practice-test-login/"
USERNAME = "student"
PASSWORD = "Password123"

# Configure Chrome options for headless execution
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

@pytest.fixture
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_successful_login(driver):
    print("Navigating to the login page...")
    # 1. Open the login page
    driver.get(URL)

    print("Entering username and password...")
    # 2. Enter username and password
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)

    print("Clicking the login button...")
    # 3. Click the login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    print("Verifying successful login...")
    # 4. Verify successful login
    success_message = driver.find_element(By.XPATH, "//div[@id='content']//h1")
    assert success_message.text == "Logged In Successfully", f"Expected 'Logged In Successfully', but got '{success_message.text}'"
    print("Login successful!")


def test_failed_login(driver):
    print("Navigating to the login page...")
    # 1. Open the login page
    driver.get(URL)

    print("Entering incorrect username and password...")
    # 2. Enter incorrect username and password
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("invalidUser")
    password_field.send_keys("invalidPassword")

    print("Clicking the login button...")
    # 3. Click the login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    print("Verifying failed login...")
    # 4. Verify failed login
    error_message = driver.find_element(By.ID, "error")
    assert error_message.text == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{error_message.text}'"
    print("Login failed as expected!")


# The following code is for running the tests using pytest from the command line
if __name__ == "__main__":
    pytest.main([__file__])
