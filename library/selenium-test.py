from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open_website(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver

def login(driver, username, password):
    login_button = driver.find_element(by=By.ID, value='Login')
    login_button.click()

    username_field = driver.find_element(by=By.XPATH, value='//*[@id="id_email"]')
    password_field = driver.find_element(by=By.NAME, value="password")
    login_button = driver.find_element(by=By.XPATH, value="/html/body/main/div/div/div/form/button")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

def verify_message(driver, message):
    time.sleep(2)
    assert message in driver.page_source

def main():
    url = "http://localhost:8000/"  # Replace with the actual website URL
    driver = open_website(url)

    valid_username = "vova270999@gmail.com"
    valid_password = "vova270999"
    invalid_password = "vova11111"
    incorrect_username = "vova111111@gmail.com"

    # Successful Login
    login(driver, valid_username, valid_password)
    verify_message(driver, "Success! You are logged in!")

    # Logout
    logout_button = driver.find_element(by=By.ID, value="Logout")
    logout_button.click()

    # Incorrect Password
    login(driver, valid_username, invalid_password)
    verify_message(driver, "ERROR! Incorrect password!")

    # Non-existing User
    login(driver, incorrect_username, invalid_password)
    verify_message(driver, "ERROR! The user does not exist, please sign up!")


    # Successful Login
    login(driver, valid_username, valid_password)
    verify_message(driver, "Success! You are logged in!")

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    main()
