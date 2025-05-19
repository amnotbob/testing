import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Define test data
USERNAME = "student"
PASSWORD = "Password123"
LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
SUCCESS_MESSAGE = "Logged In Successfully"
INVALID_USERNAME_MESSAGE = "Your username is invalid!"
INVALID_PASSWORD_MESSAGE = "Your password is invalid!"


@pytest.fixture(scope="module")
def driver():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    # Maximize window (compatible with headless mode)
    driver.maximize_window()

    yield driver

    # Teardown: Close the browser after the module tests are finished
    driver.quit()


def test_login_success(driver):
    print("Starting test_login_success")
    # Step 1: Go to the login page
    driver.get(LOGIN_URL)
    print(f"Navigated to {LOGIN_URL}")

    # Step 2: Type username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(USERNAME)
    print(f"Entered username: {USERNAME}")

    # Step 3: Type password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(PASSWORD)
    print(f"Entered password: {PASSWORD}")

    # Step 4: Click the login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Clicked login button")

    # Step 5: Check for successful login message
    success_element = driver.find_element(By.ID, "success")
    actual_message = success_element.text
    assert SUCCESS_MESSAGE in actual_message, f"Expected '{SUCCESS_MESSAGE}', but got '{actual_message}'"
    print("Login successful and message verified.")



def test_invalid_username(driver):
    print("Starting test_invalid_username")
    # Step 1: Go to the login page
    driver.get(LOGIN_URL)
    print(f"Navigated to {LOGIN_URL}")

    # Step 2: Type invalid username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("invalid_user")
    print("Entered invalid username")

    # Step 3: Type password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(PASSWORD)
    print("Entered password")

    # Step 4: Click the login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Clicked login button")

    # Step 5: Check for error message
    error_element = driver.find_element(By.ID, "error")
    actual_message = error_element.text
    assert INVALID_USERNAME_MESSAGE in actual_message, f"Expected '{INVALID_USERNAME_MESSAGE}', but got '{actual_message}'"
    print("Invalid username error message verified.")


def test_invalid_password(driver):
    print("Starting test_invalid_password")
    # Step 1: Go to the login page
    driver.get(LOGIN_URL)
    print(f"Navigated to {LOGIN_URL}")

    # Step 2: Type username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(USERNAME)
    print("Entered username")

    # Step 3: Type invalid password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("invalid_password")
    print("Entered invalid password")

    # Step 4: Click the login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Clicked login button")

    # Step 5: Check for error message
    error_element = driver.find_element(By.ID, "error")
    actual_message = error_element.text
    assert INVALID_PASSWORD_MESSAGE in actual_message, f"Expected '{INVALID_PASSWORD_MESSAGE}', but got '{actual_message}'"
    print("Invalid password error message verified.")