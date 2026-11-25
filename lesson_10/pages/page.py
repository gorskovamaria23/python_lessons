from selenium.webdriver.remote.webdriver import WebDriver


class Page:
    """Базовый класс для всех страниц проекта."""

    URL: str = ""

    def __init__(self, driver: WebDriver) -> None:
        """Сохраняет драйвер.

        Args:
            driver (WebDriver): экземпляр WebDriver.

        Returns:
            None
        """
        self.driver: WebDriver = driver

    def open(self) -> None:
        """Открывает страницу по адресу из атрибута URL.

        Returns:
            None
        """
        self.driver.get(self.URL)
