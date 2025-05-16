import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    # Setup
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()


def test_login(browser):
    # 1. Navigate to the login page
    browser.get("https://practicetestautomation.com/practice-test-login/")

    # 2. Enter username
    username_field = browser.find_element(By.ID, "username")
    username_field.send_keys("student")

    # 3. Enter password
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("Password123")

    # 4. Click the login button
    sign_in_button = browser.find_element(By.ID, "submit")
    sign_in_button.click()

    # 5. Verify successful login
    time.sleep(2) # Allow time for page to load. To be replaced with explicit wait.
    success_message = browser.find_element(By.ID, "success")
    assert success_message.is_displayed(), "Login failed"
