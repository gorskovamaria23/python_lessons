from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.page import Page


class InventoryPage(Page):
    """Page Object страницы каталога товаров."""

    URL: str = "https://www.saucedemo.com/inventory.html"
    CART_LINK = (By.ID, "shopping_cart_container")

    def add_to_cart(self, item_name: str) -> None:
        """Добавляет товар с заданным названием в корзину.

        Args:
            item_name (str): название товара.

        Returns:
            None
        """
        self.driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']"
            f"/ancestor::div[contains(@class, 'inventory_item')]//button",
        ).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину.

        Returns:
            None
        """
        self.driver.find_element(*self.CART_LINK).click()

