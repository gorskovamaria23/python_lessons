from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(2)

    name_input = driver.find_element(By.NAME, "custname")  
    name_input.send_keys("Maria")
    sleep(2)

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit_button.click()
    sleep(2)

    assert driver.current_url != "https://httpbin.qa-territory.online/forms/post"
    sleep(2)

    driver.quit()

