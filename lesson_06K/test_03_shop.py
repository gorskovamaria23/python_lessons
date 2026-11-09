from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_purchase():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")

    # 2.Авторизуйтесь как пользователь standard_user.
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Добавьте в корзину товары:
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    for name in items:
        button = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            f"//div[text()='{name}']/ancestor::div[@class='inventory_item']"
            f"//button"
        )))
        button.click()

    # 4. Перейдите в корзину
    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    # 5. Нажмите Checkout.
    driver.find_element(By.ID, "checkout").click()

    # 6. Заполните форму своими данными:
    driver.find_element(By.ID, "first-name").send_keys("Мария")
    driver.find_element(By.ID, "last-name").send_keys("Горшкова")
    driver.find_element(By.ID, "postal-code").send_keys("443000")

    # 7. Нажмите кнопку Continue.
    driver.find_element(By.ID, "continue").click()

    # 8. Прочитайте со страницы итоговую стоимость ( Total ).
    total_element = wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".summary_total_label"
    )))
    total_text = total_element.text 
    total_value = total_text.replace("Total: ", "")

    # 10. Закройте браузер.
    driver.quit()

    # 11. Проверьте, что итоговая сумма равна $58.29.
    assert total_value == "$58.29", f"Ожидалась сумма $58.29, а получено: {total_value}"