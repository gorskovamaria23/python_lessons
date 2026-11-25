import allure
import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

FIRST_NAME = "Мария"
LAST_NAME = "Горшкова"
POSTAL_CODE = "123456"

EXPECTED_TOTAL = "$58.29"


@pytest.fixture()
def driver() -> webdriver.Firefox:
    """Открывает Firefox, разворачивает окно и закрывает браузер после теста.

    Returns:
        webdriver.Firefox: экземпляр драйвера для теста.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Покупка трёх товаров в интернет-магазине")
@allure.description("Авторизуемся под standard_user, добавляем три товара в корзину, "
                    "проверяем состав корзины, оформляем заказ и сверяем итоговую "
                    "сумму с ожидаемой $58.29.")
@allure.feature("Saucedemo")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_purchase(driver: webdriver.Firefox) -> None:
    """Проверяет полный сценарий покупки: от входа до итоговой суммы.

    Args:
        driver (webdriver.Firefox): экземпляр драйвера из фикстуры.

    Returns:
        None
    """
    with allure.step("Авторизуемся под стандартным пользователем"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)

    with allure.step("Добавляем три товара в корзину и переходим в неё"):
        inventory.add_to_cart("Sauce Labs Backpack")
        inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart("Sauce Labs Onesie")
        inventory.go_to_cart()

    cart = CartPage(driver)

    with allure.step("Проверяем состав корзины"):
        items = cart.get_cart_items()
        assert len(items) == 3, f"В корзине должно быть 3 товара, а там: {items}"

    with allure.step("Оформляем заказ и заполняем данные покупателя"):
        cart.click_checkout()
        checkout = CheckOutPage(driver)
        checkout.fill_form(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    with allure.step("Проверяем итоговую сумму заказа"):
        total = checkout.get_total()
        assert total == f"Total: {EXPECTED_TOTAL}", (
            f"Ожидали {EXPECTED_TOTAL}, на странице: {total}"
        )
