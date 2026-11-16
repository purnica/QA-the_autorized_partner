from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.LandingPage import LandingPage
from pages.register import register

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

    print("Successfully Executed") 