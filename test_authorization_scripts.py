from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.LandingPage import LandingPage
from pages.register import register
from pages.SetupAccount import SetupAccount
from pages.AgencyDetails import AgencyDetails
from pages.experience import experience

@pytest.fixture()

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_authorization_scripts(driver):

    # clicking register btn from the landing page
    obj1 = LandingPage(driver)
    obj1.open_url("https://authorized-partner.vercel.app/")
    assert driver.find_element(By.TAG_NAME, "button").is_displayed()
    obj1.click_signupbtn()

    # verifing if the page is succesfully loaded
    assert "register" in driver.current_url, "Failed"

    # clicking the checkbox and continue btn
    obj2 = register(driver)
    obj2.checkbox_terms()
    obj2.click_continue()

    # verify if the page sucessfully loads to the setup page
    assert "setup" in driver.current_url, "Failed"

    # entering all the details
    obj3 = SetupAccount(driver)
    obj3.enter_firstname("Purnika")
    obj3.enter_lastname("Prajapati")
    obj3.enter_email("viritpurnika@yopmail.com")
    obj3.enter_contact(9841385333)
    obj3.enter_password("Pa$$w0rd!")
    obj3.enter_confirmPassword("Pa$$w0rd!")
    obj3.click_nextbtn()

    wait = WebDriverWait(driver, 100)
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"),"Email Verification code"))

    assert "Email Verification code" in driver.page_source, "page not loaded" 

    obj4 = AgencyDetails(driver)
    obj4.enter_name("ABC Agency")
    obj4.enter_role("Manager")
    obj4.enter_email("abc@agency.com")
    obj4.enter_website("https://abc.com")
    obj4.enter_address("Lalitpur")
    obj4.enter_region("Nepal")
    obj4.click_nextbtn()

    assert "professional-experience" in driver.current_url, "failed"

    obj5 = experience(driver)
    obj5.select_experience("5 years")
    obj5.enter_studentnum("200")
    obj5.enter_focus("Undergraduate admissions to Canada")
    obj5.enter_metrics("90")
    obj5.select_services(["Career Counseling", "Visa Processing"])
    obj5.click_nextbtn()
