import pytest
from selenium import webdriver
from pages.calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    page.open()

    page.set_delay(45)

    for button in ["7", "+", "8", "="]:
        page.press(button)

    result = page.wait_for_result("15")
    assert result == "15", f"Ожидали 15, на экране: {result}"
