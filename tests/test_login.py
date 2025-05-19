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


def test_successful_login(driver):
    # 1. Navigate to the URL
    url = "https://practicetestautomation.com/practice-test-login/"
    driver.get(url)

    try:
        # 2. Enter a valid username in the username field.
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        # 3. Enter the correct password in the password field.
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # 4. Click the submit/login button.
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 5. Verify that the page shows a message confirming successful login
        actual_confirmation_message = driver.find_element(By.XPATH, "//div[@id='content']//h1").text
        assert "Logged In Successfully" in actual_confirmation_message

    except Exception as e:
        print("Error: ", str(e))
        raise
