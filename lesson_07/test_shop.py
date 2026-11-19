import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


FIRST_NAME = "Мария"
LAST_NAME = "Горшкова"
POSTAL_CODE = "123456"

EXPECTED_TOTAL = "$58.29"


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_to_cart("Sauce Labs Backpack")
    inventory.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory.add_to_cart("Sauce Labs Onesie")

    inventory.go_to_cart()
    cart = CartPage(driver)
    items = cart.get_cart_items()
    assert len(items) == 3, f"В корзине должно быть 3 товара, а там: {items}"

    cart.click_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_form(FIRST_NAME, LAST_NAME, POSTAL_CODE)

    total = checkout.get_total()
    assert total == f"Total: {EXPECTED_TOTAL}", (
        f"Ожидали {EXPECTED_TOTAL}, а на странице: {total}"
    )
