import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


def test_login_success(driver):
    # 1. Go to the website
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Navigated to the login page")

    # 2. Type a valid username into the username box
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")
    print("Entered username")

    # 3. Type the correct password into the password box
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")
    print("Entered password")

    # 4. Click the login or submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Clicked submit button")

    # 5. Check if the page shows a success message
    try:
        success_message = driver.find_element(By.XPATH, "//div[@id='content']//h1")
        assert success_message.text == "Logged In Successfully", f"Expected 'Logged In Successfully', but got '{success_message.text}'"
        print("Login successful!")
    except Exception as e:
        print("Error: ", str(e))
        assert False, "Login failed: Could not find success message"


def test_login_failure(driver):
    # 1. Go to the website
    driver.get("https://practicetestautomation.com/practice-test-login/")
    print("Navigated to the login page")

    # 2. Type an invalid username into the username box
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("wronguser")
    print("Entered incorrect username")

    # 3. Type an incorrect password into the password box
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("WrongPassword")
    print("Entered incorrect password")

    # 4. Click the login or submit button
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    print("Clicked submit button")

    # 5. Check if there is an error message
    try:
        error_message = driver.find_element(By.ID, "error")
        assert error_message.text == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{error_message.text}'"
        print("Login failure test passed!")
    except Exception as e:
        print("Error: ", str(e))
        assert False, "Login passed, but should have failed"


if __name__ == "__main__":
    pytest.main([__file__])