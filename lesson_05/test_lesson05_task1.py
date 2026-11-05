from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_lesson05_task1():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    driver.maximize_window()
    sleep(3)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(2)

    assert "/forms/post" in driver.current_url
    
    driver.back()

    assert driver.current_url == "https://httpbin.qa-territory.online/"
    sleep(2)

    driver.quit()