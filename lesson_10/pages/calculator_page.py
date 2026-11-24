from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.page import Page


class CalculatorPage(Page):
    """Page Object страницы «Slow calculator»."""

    URL: str = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    SCREEN = (By.CSS_SELECTOR, ".screen")
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")

    def set_delay(self, seconds: int) -> None:
        """Задаёт задержку вычисления в секундах.

        Args:
            seconds (int): задержка в секундах.

        Returns:
            None
        """
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(str(seconds))

    def press(self, button: str) -> None:
        """Нажимает кнопку калькулятора с заданным текстом.

        Args:
            button (str): надпись на кнопке, например "7" или "+".

        Returns:
            None
        """
        self.driver.find_element(
            By.XPATH, f"//span[normalize-space(text())='{button}']"
        ).click()

    def get_result(self) -> str:
        """Возвращает текст на экране калькулятора.

        Returns:
            str: текущее значение на экране.
        """
        return self.driver.find_element(*self.SCREEN).text
