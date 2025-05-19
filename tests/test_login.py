import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox") # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource

    # Instantiate Chrome WebDriver with options
    service = Service(executable_path='/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver

    driver.quit()


def test_login(driver):
    # Define the URL
    url = "https://practicetestautomation.com/practice-test-login/"

    # Define valid credentials
    username = "student"
    password = "Password123"

    try:
        # 1. Go to the website
        print("Navigating to URL...")
        driver.get(url)

        # 2. Type username into the username box
        print("Entering username...")
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)

        # 3. Type password into the password box
        print("Entering password...")
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # 4. Click the login button
        print("Clicking submit button...")
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 5. Check if the page shows a success message
        print("Checking for successful login...")
        success_message = driver.find_element(By.ID, "content")
        assert "Logged In Successfully" in success_message.text or "Welcome" in success_message.text
        print("Login successful!")

    except Exception as e:
        print("Error: ", str(e))
        assert False, f"Test failed due to exception: {str(e)}"

    finally:
        print("Test completed.")
