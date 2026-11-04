from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # 2. В поле #delay введите значение 45
    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    # 3. Нажимите кнопки: 7 + 8 =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # 4. Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result_element = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result.strip() == "15", f"Ожидался результат 15, а получено: {result}"

    driver.quit()
