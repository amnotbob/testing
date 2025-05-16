import time
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

def test_login_success(driver):
    # Navigate to login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter username and password
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("student")
    password_field.send_keys("Password123")

    # Click login button
    sign_in_button = driver.find_element(By.ID, "submit")
    sign_in_button.click()

    # Verify successful login
    time.sleep(2)
    assert driver.current_url == "https://practicetestautomation.com/practice-test-login/"
    success_message = driver.find_element(By.XPATH, "//div[@id='content']//h1").text
    assert success_message == "Logged In Successfully"

def test_login_failure(driver):
    # Navigate to login page
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter username and password
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    username_field.send_keys("wrong_user")
    password_field.send_keys("wrong_password")

    # Click login button
    sign_in_button = driver.find_element(By.ID, "submit")
    sign_in_button.click()

    # Verify unsuccessful login
    time.sleep(2)
    assert driver.current_url == "https://practicetestautomation.com/practice-test-login/"
    error_message = driver.find_element(By.ID, "error").text
    assert error_message == "Your username is invalid!"
