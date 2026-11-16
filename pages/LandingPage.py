from selenium.webdriver.common.by import By
import time

class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.signupBtn = (By.TAG_NAME, "button")

    def open_url(self, url):
        self.driver.get(url)
        time.sleep(2)    

    def click_signupbtn(self):
        self.driver.find_element(*self.signupBtn).click()
        time.sleep(2)


