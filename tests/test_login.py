import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_login(driver):
    # Navigate to the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    try:
        # Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys("student")

        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # Click submit
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # Verify login result
        info_element = driver.find_element(By.ID, "info")
        actual_result = info_element.text

        assert "Logged In Successfully" in actual_result or "failed" in actual_result

    except Exception as e:
        print("Error: ", str(e))
        assert False, f"Test failed due to exception: {str(e)}"
    finally:
        print("Test completed")