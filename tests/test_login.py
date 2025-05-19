import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    # Setup: Launch the browser
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    # Teardown: Close the browser after the test
    driver.quit()

def test_login_page(driver):
    # 1. Navigate to the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    # 2. Enter username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")
    time.sleep(2)

    # 3. Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    time.sleep(2)

    # 4. Click Submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(2)

    # 5. Verify successful login
    text_locator = driver.find_element(By.ID, "content")
    actual_text = text_locator.text

    assert "Logged In Successfully" in actual_text or "failed" in actual_text