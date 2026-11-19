from selenium.webdriver.common.by import By


class InventoryPage:
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    ADD_TO_CART_BUTTONS = {
        "Sauce Labs Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Sauce Labs Bolt T-Shirt": (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
        ),
        "Sauce Labs Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
    }

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        locator = self.ADD_TO_CART_BUTTONS[product_name]
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
