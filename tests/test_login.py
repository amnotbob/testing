import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_login(driver):
    # Navigate to the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")

    # Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")

    # Click submit
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    # Verify login status
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "success")))
        success_message = driver.find_element(By.ID, "success")
        assert "Logged In Successfully" in success_message.text
        print("Login successful!")
    except:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "error")))
            error_message = driver.find_element(By.ID, "error")
            assert "failed" in error_message.text
            print("Login failed!")
        except:
            print("Login status unknown!")
            assert False # force fail if neither success nor failure is found
