import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def browser():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    # Add any other options you may need, like window size
    service = Service(executable_path="/usr/bin/chromedriver") # Or the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


@pytest.mark.parametrize("username, password, expected_result", [
    ("student", "Password123", "Logged In Successfully"),
    ("invalid", "invalid", "Invalid username or password")
])
def test_login(browser, username, password, expected_result):
    try:
        # Navigate to the webpage
        browser.get("https://practicetestautomation.com/practice-test-login/")

        # Enter username
        username_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_field.send_keys(username)

        # Enter password
        password_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_field.send_keys(password)

        # Click login button
        login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
        login_button.click()

        # Verify login success or failure
        message_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "error")))
        if expected_result == "Logged In Successfully":
            message_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.LINK_TEXT, expected_result)))
            assert expected_result in message_element.text, "Login failed"
        else:
            assert expected_result in message_element.text, "Login failed"

    except Exception as e:
        pytest.fail(f"Test failed: {e}")
