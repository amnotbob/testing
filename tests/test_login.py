import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup
@pytest.fixture(scope='module')
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://practicetestautomation.com/practice-test-login/")
    yield driver
    driver.quit()

# Test case
def test_login(driver):
    # Enter username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")
    print("Entered username")

    # Enter password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    print("Entered password")

    # Click login button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Clicked login button")

    # Check login result
    try:
        success_message = driver.find_element(By.XPATH, "//div[@id='content']//h1[text()='Logged In Successfully']")
        assert success_message.is_displayed()
        print("Login successful")
    except:
        try:
            error_message = driver.find_element(By.ID, "error")
            assert error_message.is_displayed()
            print("Login failed: " + error_message.text)
        except Exception as e:
            print("Error: ", str(e))
            assert False, f"Login failed and no error message was found. Exception: {e}"

