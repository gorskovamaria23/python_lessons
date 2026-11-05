from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    cookie_user_1 = {"name": "SESSION", "value": "ZDFlMzkzMWYtYzA4OS00ZDVhLTk4NDAtMDc3ZTU2MDBhYzFi", "domain": "gitflic.ru"}
    cookie_user_2 = {"name": "SESSION", "value": "NWU1YTA5ODAtYmQ3ZC00OWY2LTkwNzgtNTliZmIzMTY3YmMx", "domain": "gitflic.ru"}
    base_url = "https://gitflic.ru/"  

#1.Откройте страницу https://gitflic.ru/.
    driver.get(base_url)
#2.Установите cookie пользователя 1.
    driver.add_cookie(cookie_user_1)
#3.Обновите страницу.
    driver.refresh()
#4.Перейдите на страницу пользователя 1.
    driver.get("https://gitflic.ru/user/1user")
#5Сохраните текущий URL.
    url_user1 = driver.current_url
    print(f"URL пользователя 1: {url_user1}")

# 6.Удаляем все cookies (выходим из аккаунта)
    driver.delete_all_cookies()

#7.Установите cookie пользователя 2.
    driver.get(base_url)
    driver.add_cookie(cookie_user_2)
#8.Обновите страницу.
    driver.refresh()
#9.Перейдите на страницу пользователя 2.
    driver.get("https://gitflic.ru/user/2user")

#10.Сохраните текущий URL.
    url_user2 = driver.current_url
    print(f"URL пользователя 2: {url_user2}")

#11.Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2, f"Ошибка: URL совпали! {url_user1} == {url_user2}"
    
    driver.quit()
