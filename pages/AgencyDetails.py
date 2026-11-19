from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AgencyDetails:
    def __init__(self, driver):
            self.driver = driver
            self.name = (By.NAME, "agency_name")
            self.role = (By.NAME, "role_in_agency")
            self.email = (By.NAME, "agency_email")
            self.website = (By.NAME, "agency_website")
            self.address = (By.NAME, "agency_address")
            self.region = (By.XPATH,"//button[@role='combobox']")
            self.region_search = (By.XPATH, "///input[@placeholder='Search...']")
            self.nextBtn = (By.XPATH, "//button[normalize-space()='Next']")

    def _region_option(self):
        return (By.XPATH, f"//*[@role='option' and normalize-space()='Nepal']")
    
    def enter_name(self, name):
            self.driver.find_element(*self.name).send_keys(name)

    def enter_role(self, role):
            self.driver.find_element(*self.role).send_keys(role)

    def enter_email(self, email):
            self.driver.find_element(*self.email).send_keys(email)

    def enter_website(self, website):
            self.driver.find_element(*self.website).send_keys(website)

    def enter_address(self, address):
            self.driver.find_element(*self.address).send_keys(address)

    def enter_region(self, region_name):
        self.wait.until(EC.element_to_be_clickable(self.region)).click()

        search = self.wait.until(EC.visibility_of_element_located(self.region_search))
        search.send_keys(region_name)

        self.wait.until(EC.element_to_be_clickable(self._region_option(region_name))).click()

    def click_nextbtn(self):
            self.driver.find_element(*self.nextBtn).click()
            time.sleep(5)
