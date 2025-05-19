import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    # Setup: Launch browser
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    # Teardown: Close browser after each test
    driver.quit()


def test_login_success(driver):
    try:
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
        confirmation_element = driver.find_element(By.ID, "confirmation")
        assert confirmation_element.text == "Logged In Successfully", "Login failed"

    except Exception as e:
        print("Error: ", str(e))
        raise
    finally:
        pass
