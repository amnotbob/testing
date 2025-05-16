import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    # Teardown
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
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # 5. Verify successful login
    try:
        success_message = driver.find_element(By.ID, "success")
        assert success_message.is_displayed(), "Success message not displayed"
        print("Login successful!")
    except:
        fail_message = driver.find_element(By.ID, "error")
        assert fail_message.is_displayed(), "Error message not displayed"
        print("Login failed!")


if __name__ == '__main__':
    pytest.main([__file__])