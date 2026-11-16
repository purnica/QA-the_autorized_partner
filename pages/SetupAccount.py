from selenium.webdriver.common.by import By
import time

class SetupAccount:
    def __init__(self, driver):
            self.driver = driver
            self.firstname = (By.NAME, "firstName")
            self.lastname = (By.NAME, "lastName")
            self.email = (By.NAME, "email")
            self.contact = (By.NAME, "phoneNumber")
            self.password = (By.NAME, "password")
            self.confirmPassword = (By.NAME, "confirmPassword")
            self.nextBtn = (By.XPATH, "//button[normalize-space()='Next']")

    def enter_firstname(self, firstname):
            self.driver.find_element(*self.firstname).send_keys(firstname)

    def enter_lastname(self, lastname):
            self.driver.find_element(*self.lastname).send_keys(lastname)

    def enter_email(self, email):
            self.driver.find_element(*self.email).send_keys(email)

    def enter_contact(self, contact):
            self.driver.find_element(*self.contact).send_keys(contact)

    def enter_password(self, password):
            self.driver.find_element(*self.password).send_keys(password)

    def enter_confirmPassword(self, confirmPassword):
            self.driver.find_element(*self.confirmPassword).send_keys(confirmPassword)

    def click_nextbtn(self):
            self.driver.find_element(*self.nextBtn).click()
            time.sleep(5)
