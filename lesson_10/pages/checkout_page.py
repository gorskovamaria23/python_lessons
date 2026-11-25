from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.page import Page


class CheckOutPage(Page):
    """Page Object страниц оформления заказа."""

    URL: str = "https://www.saucedemo.com/checkout-step-one.html"
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Заполняет форму данными покупателя и нажимает «Continue».

        Args:
            first_name (str): имя.
            last_name (str): фамилия.
            postal_code (str): почтовый индекс.

        Returns:
            None
        """
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа.

        Returns:
            str: текст вида "Total: $58.29".
        """
        return self.driver.find_element(*self.TOTAL_LABEL).text
