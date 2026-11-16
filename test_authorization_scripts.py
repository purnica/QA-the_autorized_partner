from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.LandingPage import LandingPage

@pytest.fixture()

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_authorization_scripts(driver):
    obj = LandingPage(driver)

    obj.open_url("https://authorized-partner.vercel.app/")

    assert driver.find_element(By.TAG_NAME, "button").is_displayed()

    obj.click_signupbtn()

    assert "register" in driver.current_url, "Failed"

    

    print("Successfully Executed") 