import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    # Initialize the Chrome driver
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s, options=chrome_options)
    yield driver
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

    # 4. Click the login button
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    # 5. Verify the login result
    text_element = driver.find_element(By.ID, "content")
    actual_text = text_element.text

    assert "Logged In Successfully" in actual_text or "failed" in actual_text