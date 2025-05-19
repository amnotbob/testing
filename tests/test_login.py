import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
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

    # 4. Click submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 5. Verify successful login
    time.sleep(2)  # Give the page time to load.  Consider using WebDriverWait for more reliability
    success_message = driver.find_element(By.ID, "success")
    assert "Logged In Successfully" in success_message.text or "failed" in success_message.text


if __name__ == '__main__':
    pytest.main([__file__])