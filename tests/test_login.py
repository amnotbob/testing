import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Setup
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    # Teardown
    driver.quit()

def test_login(driver):
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
        success_text = driver.find_element(By.ID, "content")
        assert "Logged In Successfully" in success_text.text

    except Exception as e:
        print("Error: ", str(e))
    finally:
        pass
