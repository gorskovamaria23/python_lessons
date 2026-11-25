import time

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
        field.send_keys(seconds)

    def press(self, button: str) -> None:
        """Нажимает кнопку калькулятора по её тексту.

        Args:
            button (str): символ на кнопке: цифра, "+" или "=".

        Returns:
            None
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{button}']"
        ).click()

    def get_result(self) -> str:
        """Возвращает текущий текст на экране калькулятора.

        Returns:
            str: текст на экране, например "15" или "Pending operation...".
        """
        return self.driver.find_element(*self.SCREEN).text

    def wait_for_result(self, expected: str, timeout: int = 60, interval: float = 0.5) -> str:
        """Опрашивает экран калькулятора, пока не появится ожидаемый результат.

        Args:
            expected (str): ожидаемый текст на экране, например "15".
            timeout (int): максимальное время ожидания в секундах.
            interval (float): пауза между опросами экрана в секундах.

        Returns:
            str: фактический текст на экране калькулятора.

        Raises:
            TimeoutError: если за отведённое время результат не появился.
        """
        deadline = time.time() + timeout

        while time.time() < deadline:
            result = self.get_result()

            if result == expected:
                return result

            time.sleep(interval)

        raise TimeoutError(
            f"За {timeout} секунд на экране не появилось '{expected}'. "
            f"Последнее значение: '{self.get_result()}'"
        )

