from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.page import Page


class CartPage(Page):
    """Page Object страницы корзины."""

    URL: str = "https://www.saucedemo.com/cart.html"
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items(self) -> List[str]:
        """Возвращает список названий товаров в корзине.

        Returns:
            List[str]: названия товаров.
        """
        elements = self.driver.find_elements(*self.CART_ITEMS)
        return [item.text for item in elements]

    def click_checkout(self) -> None:
        """Нажимает кнопку «Checkout».

        Returns:
            None
        """
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
