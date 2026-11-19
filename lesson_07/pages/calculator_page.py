from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(str(seconds))

    def press(self, button):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button}']"
        ).click()

    def get_screen_text(self):
        return self.driver.find_element(*self.SCREEN).text

    def wait_for_result(self, expected):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self.get_screen_text()
