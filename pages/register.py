from selenium.webdriver.common.by import By
import time

class register:
    def __init__(self, driver):
        self.driver = driver
        self.terms = (By.ID, "remember")
        self.continueBtn = (By.LINK_TEXT, "Continue")

    def checkbox_terms(self):
        self.driver.find_element(*self.terms).click()
        time.sleep(2)

    def click_continue(self):
        self.driver.find_element(*self.continueBtn).click()
        time.sleep(2)