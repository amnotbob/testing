import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def browser():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless') # Run in headless mode
    # Add any other options you may need, like window size
    service = Service(executable_path="/usr/bin/chromedriver") # Or the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()



def test_login(browser):
    try:
        # Navigate to the webpage
        browser.get("webpage-link")  # Replace with your actual URL

        # Enter username
        username_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username"))) # Replace with correct ID or other locator
        username_field.send_keys("student")

        # Enter password
        password_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password"))) # Replace with correct ID or other locator
        password_field.send_keys("Password123")

        # Click login button
        login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "login_button")))  # Replace with correct ID or other locator
        login_button.click()

        # Verify login success
        success_message = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "success_message")))  # Replace with correct ID or other locator
        assert "Logged In Successfully" in success_message.text, "Login failed"

    except Exception as e:
        pytest.fail(f"Test failed: {e}")
    finally:
        pass # Optional: Add cleanup if needed
