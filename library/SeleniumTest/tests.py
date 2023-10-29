import time
import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from authentication.models import CustomUser


def register_user(first_name, middle_name, last_name, email, password):
    user = CustomUser.create(first_name=first_name,
                                          middle_name=middle_name,
                                          last_name=last_name,
                                          email=email,
                                          password=password)
    user.save()
    if user:
        return True
    else:
        return False


def delete_user():
    user = CustomUser.objects.filter(email="john.doe@example.com").first()
    user = CustomUser.delete_by_id(user.id)
    user.save()
    if user:
        return True


class SeleniumTest(LiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Initialize the WebDriver
        self.driver.maximize_window()  # Maximize the browser window


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()  # Close the WebDriver

    def test_registration(self):
        driver = self.driver

        # Step 1: Open the website
        driver.get(self.live_server_url)

        # Step 2: Click on the "Register" link
        register_link = driver.find_element(by=By.LINK_TEXT, value='Register')
        register_link.click()
        time.sleep(3)
        # Step 3: Fill in the registration form
        first_name_field = driver.find_element(by=By.ID, value='id_first_name')
        middle_name_field = driver.find_element(by=By.ID, value='id_middle_name')
        last_name_field = driver.find_element(by=By.ID, value='id_last_name')
        email_field = driver.find_element(by=By.ID, value='id_email')
        password_field = driver.find_element(by=By.ID, value='id_password')
        role_field = driver.find_element(by=By.ID, value='id_role')
        submit_button = driver.find_element(by=By.NAME, value='submit_action')

        first_name_field.send_keys("John")
        middle_name_field.send_keys("Middle")
        last_name_field.send_keys("Doe")
        email_field.send_keys("john.doe@example.com")
        password_field.send_keys("password123")
        # Choose the appropriate role (e.g., "visitor" or "librarian")
        select = Select(driver.find_element(by=By.ID, value='id_role'))
        select.select_by_visible_text('librarian')
        time.sleep(1)
        submit_button.click()
        time.sleep(3)
        # Step 4: Verify successful registration
        self.assertIn("Registration successful!", driver.page_source)

        register_user(first_name="Vova",
                      middle_name="Serg",
                      last_name="Potap",
                      email="vova270999@gmail.com",
                      password="vova270999",
                      )

        # Step 5: Click on the "Logout" button
        logout_button = driver.find_element(by=By.ID, value='UsersInfo')
        logout_button.click()
        time.sleep(5)

        # Step 5: Click on the "Logout" button
        logout_button = driver.find_element(by=By.ID, value="Logout")
        logout_button.click()
        time.sleep(3)

        # Step 6: Verify successful logout
        expected_message = "Logged out!"
        print("Expected message:", expected_message)
        self.assertIn(expected_message, driver.page_source)


    def test_login_and_logout(self):

        register_user(first_name="Marko",
                      middle_name="Middle",
                      last_name="Doe",
                      email="marko.doe@example.com",
                      password="password123"
                      )

        driver = self.driver

        # Step 1: Open the website
        driver.get(self.live_server_url)  # Use the live_server_url provided by LiveServerTestCase
        time.sleep(3)

        # Step 2: Click on the "Login" button
        login_button = driver.find_element(by=By.ID, value='Login')
        login_button.click()
        time.sleep(1)

        # Step 3: Enter valid login credentials and click "Login"
        username_field = driver.find_element(by=By.XPATH, value='//*[@id="id_email"]')
        password_field = driver.find_element(by=By.NAME, value="password")
        login_button = driver.find_element(by=By.XPATH, value="/html/body/main/div/div/div/form/button")
        time.sleep(1)

        username_field.send_keys("marko.doe@example.com")
        password_field.send_keys("password123")
        login_button.click()
        time.sleep(1)

        # Step 4: Verify successful login
        expected_message = "Success! You are logged in!"
        print("Expected message:", expected_message)
        self.assertIn(expected_message, driver.page_source)
        time.sleep(1)

        # Step 5: Click on the "Logout" button
        logout_button = driver.find_element(by=By.ID, value="Logout")
        logout_button.click()
        time.sleep(1)

        # Step 6: Verify successful logout
        expected_message = "Logged out!"
        print("Expected message:", expected_message)
        self.assertIn(expected_message, driver.page_source)


    def test_invalid_login(self):
        register_user(first_name="John",
                      middle_name="Middle",
                      last_name="Doe",
                      email="john.doe@example.com",
                      password="password123"
                      )

        driver = self.driver

        # Step 1: Open the website
        driver.get(self.live_server_url)
        time.sleep(1)

        # Step 2: Click on the "Login" button
        login_button = driver.find_element(by=By.ID, value='Login')
        login_button.click()
        time.sleep(1)

        # Step 3: Enter invalid login credentials and click "Login"
        username_field = driver.find_element(by=By.XPATH, value='//*[@id="id_email"]')
        password_field = driver.find_element(by=By.NAME, value="password")
        login_button = driver.find_element(by=By.XPATH, value="/html/body/main/div/div/div/form/button")
        time.sleep(1)

        username_field.send_keys("john.doe@example.com")
        password_field.send_keys("vova11111")
        time.sleep(1)
        login_button.click()

        # Step 4: Verify unsuccessful login and error message
        expected_message = "ERROR! Incorrect password!"
        print("Expected message:", expected_message)
        self.assertIn(expected_message, driver.page_source)

    def test_user_does_not_exist(self):
        register_user(first_name="John",
                      middle_name="Middle",
                      last_name="Doe",
                      email="john.doe@example.com",
                      password="password123"
                      )

        driver = self.driver

        # Step 1: Open the website
        driver.get(self.live_server_url)
        time.sleep(1)

        # Step 2: Click on the "Login" button
        login_button = driver.find_element(by=By.ID, value='Login')
        login_button.click()
        time.sleep(1)

        # Step 3: Enter invalid login credentials and click "Login"
        username_field = driver.find_element(by=By.XPATH, value='//*[@id="id_email"]')
        password_field = driver.find_element(by=By.NAME, value="password")
        login_button = driver.find_element(by=By.XPATH, value="/html/body/main/div/div/div/form/button")
        time.sleep(1)

        username_field.send_keys("nooneknows@mail.com")
        password_field.send_keys("vova11111")
        login_button.click()

        # Step 4: Verify unsuccessful login and error message
        expected_message = 'ERROR! The user does not exist, please sign up!'
        print("Expected message:", expected_message)
        self.assertIn(expected_message, driver.page_source)


    # def test_delete_user(self):
    #     register_user(first_name="John",
    #                   middle_name="Middle",
    #                   last_name="Doe",
    #                   email="john.doe@example.com",
    #                   password="password123")
    #
    #     register_user(first_name="Amanda",
    #                   middle_name="Pokes",
    #                   last_name="Megucho",
    #                   email="amanda.pokes@example.com",
    #                   password="password123")
    #
    #     driver = self.driver
    #
    #     # Step 1: Open the website
    #     driver.get(self.live_server_url)
    #
    #     # Step 2: Click on the "Login" button
    #     login_button = driver.find_element(by=By.ID, value='Login')
    #     login_button.click()
    #     time.sleep(1)
    #
    #     # Step 3: Enter valid login credentials and click "Login"
    #     username_field = driver.find_element(by=By.XPATH, value='//*[@id="id_email"]')
    #     password_field = driver.find_element(by=By.NAME, value="password")
    #     login_button = driver.find_element(by=By.XPATH, value="/html/body/main/div/div/div/form/button")
    #     time.sleep(1)
    #
    #     username_field.send_keys("john.doe@example.com")
    #     password_field.send_keys("password123")
    #     login_button.click()
    #     time.sleep(1)
    #
    #     # Step 2: Click on the "UsersInfo" link
    #     driver.get(self.live_server_url)
    #     # Step 5: Click on the "Logout" button
    #     logout_button = driver.find_element(by=By.ID, value='UsersInfo')
    #     logout_button.click()
    #     time.sleep(5)
    #
    #
    #     # Step 3: Find the user to delete and click on the "Delete" button
    #     user_rows = driver.find_elements(by=By.XPATH, value="//table[@class='table user-table']/tbody/tr")
    #     for row in user_rows:
    #         columns = row.find_elements(by=By.TAG_NAME, value='td')
    #         if columns[0].text == "Amanda" and columns[1].text == "Pokes" and columns[3].text == "amanda.pokes@example.com":
    #             delete_button = row.find_element(by=By.ID, value='Delete user')
    #             delete_button.click()
    #             break
    #
    #     # Step 5: Verify successful deletion
    #     self.assertNotIn("User has been deleted successfully!", driver.page_source)
    #
    #     # Step 5: Click on the "Logout" button
    #     logout_button = driver.find_element(by=By.ID, value="Logout")
    #     logout_button.click()
    #     time.sleep(3)



if __name__ == "__main__":
    unittest.main()
