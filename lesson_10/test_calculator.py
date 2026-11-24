import time

import allure
import pytest
from selenium import webdriver

from pages.calculator_page import CalculatorPage


@pytest.fixture()
def driver() -> webdriver.Chrome:
    """Открывает Chrome, разворачивает окно и закрывает браузер после теста.

    Returns:
        webdriver.Chrome: экземпляр драйвера для теста.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Медленный калькулятор считает 7 + 8 = 15")
@allure.description("Устанавливаем задержку вычислений 45 секунд, нажимаем "
                    "кнопки 7, +, 8, = и дожидаемся результата 15 на экране.")
@allure.feature("Slow calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver: webdriver.Chrome) -> None:
    """Проверяет корректность вычисления 7 + 8 при задержке 45 секунд.

    Args:
        driver (webdriver.Chrome): экземпляр драйвера из фикстуры.

    Returns:
        None
    """
    page = CalculatorPage(driver)

    with allure.step("Открываем страницу калькулятора"):
        page.open()

    with allure.step("Устанавливаем задержку вычисления 45 секунд"):
        page.set_delay(45)

    with allure.step("Нажимаем кнопки 7, +, 8, ="):
        for button in ["7", "+", "8", "="]:
            page.press(button)

    with allure.step("Проверяем, что на экране появилось 15"):
        time.sleep(50)  # ждём, пока калькулятор досчитает с задержкой 45 секунд
        result = page.get_result()
        assert result == "15", f"Ожидали 15, на экране: {result}"
