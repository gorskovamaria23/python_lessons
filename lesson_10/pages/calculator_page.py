from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

    def wait_for_result(self, expected: str, timeout: int = 60) -> str:
        """Дожидается появления ожидаемого результата на экране калькулятора.

        Использует явное ожидание WebDriverWait: проверка повторяется
        автоматически, пока на экране не появится нужное значение.

        Args:
            expected (str): ожидаемый текст на экране, например "15".
            timeout (int): максимальное время ожидания в секундах.

        Returns:
            str: фактический текст на экране калькулятора.

        Raises:
            TimeoutException: если за отведённое время результат не появился.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self.get_result()

