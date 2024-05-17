from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

print("Добро пожаловать в Википедию!")
browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')

while True:
    query = input(f"Введите поисковый запрос: ")
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.clear()
    search_box.send_keys(query)
    time.sleep(2)
    search_box.send_keys(Keys.RETURN)
    choice = input(f"- листать далее - 'l'\n- перейти на одну из связанных страниц - 'g'\n- выйти из программы - 'q'")
    if choice == "q":
        print("Спасибо за участие!")
        break
    elif choice == "l":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            input()
    elif choice == "g":
        links = browser.find_elements(By.TAG_NAME, "a")
        # for link in links:
        #     print(link)
        link = links[1].get_attribute("href") #выберите
        browser.get(link)
        time.sleep(2)

