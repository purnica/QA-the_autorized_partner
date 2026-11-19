from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class experience:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        # Anchor to the combobox button (no stable id/name available)
        self.experience = (By.XPATH, "//button[@role='combobox']")
        self.studentnum = (By.NAME, "number_of_students_recruited_annually")
        self.focus = (By.NAME, "focus_area")
        self.metrics = (By.NAME, "success_metrics")
        self.nextBtn = (By.XPATH, "//button[normalize-space()='Next']")

    # ---------- Dynamic locators ----------
    def _experience_option(self, years_text):
        # Popup is rendered in a portal, so search the whole page
        return (By.XPATH, f"//*[@role='option' and normalize-space()='{years_text}']")

    def _service_checkbox(self, service_name):
        # Finds the checkbox button that sits next to the label text
        return (
            By.XPATH,
            f"//label[normalize-space()='{service_name}']/..//button[@role='checkbox']",
        )

    # ---------- Actions ----------
    def select_experience(self, years_text):
        """years_text examples: '1 year', '5 years', '10+ years'"""
        self.wait.until(EC.element_to_be_clickable(self.experience)).click()
        self.wait.until(
            EC.element_to_be_clickable(self._experience_option(years_text))
        ).click()
        # Wait for the popup to close
        self.wait.until(
            EC.invisibility_of_element_located(self._experience_option(years_text))
        )

    def enter_studentnum(self, studentnum):
        field = self.wait.until(EC.visibility_of_element_located(self.studentnum))
        field.clear()
        field.send_keys(studentnum)

    def enter_focus(self, focus):
        field = self.wait.until(EC.visibility_of_element_located(self.focus))
        field.clear()
        field.send_keys(focus)

    def enter_metrics(self, metrics):
        field = self.wait.until(EC.visibility_of_element_located(self.metrics))
        field.clear()
        field.send_keys(metrics)

    def select_service(self, service_name, checked=True):
        """Make a service checkbox checked/unchecked, whatever its current state."""
        checkbox = self.wait.until(
            EC.element_to_be_clickable(self._service_checkbox(service_name))
        )
        is_checked = checkbox.get_attribute("aria-checked") == "true"
        if is_checked != checked:
            checkbox.click()

    def select_services(self, services):
        """Pass the list you want checked; all other services get unchecked."""
        all_services = [
            "Career Counseling",
            "Admission Applications",
            "Visa Processing",
            "Test Prepration",  # spelled as shown on the page
        ]
        for service in all_services:
            self.select_service(service, checked=service in services)

    def click_nextbtn(self):
        self.wait.until(EC.element_to_be_clickable(self.nextBtn)).click()