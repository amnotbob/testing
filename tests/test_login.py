import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    # Setup Chrome options for headless mode (optional, but good for CI/CD)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off
    chrome_options.add_argument("--no-sandbox") # overcome limited resource error
    chrome_options.add_argument("--disable-dev-shm-usage") # resolves crashing

    # Set up ChromeDriver service
    s = Service('./chromedriver')  # Path to your chromedriver

    # Initialize WebDriver with options and service
    driver = webdriver.Chrome(service=s, options=chrome_options)
    yield driver
    driver.quit()

def test_login(driver):
    # Test case for successful login
    try:
        # 1. Navigate to the login page
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 2. Enter username and password
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        username_field.send_keys("student")
        password_field.send_keys("Password123")

        # 3. Click the login button
        submit_button = driver.find_element(By.ID, "submit")
        submit_button.click()

        # 4. Verify successful login
        success_message = driver.find_element(By.XPATH, "//div[@id='content']//h1")
        assert success_message.text == "Logged In Successfully", "Login was not successful"

    except Exception as e:
        print("Error: ", str(e))
        assert False, f"Test failed due to exception: {str(e)}"