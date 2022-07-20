import time 
from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера.
driver = webdriver.Chrome()
time.sleep(20)
# открываем страницу
driver.get("https://stepik.org/lesson/25969/step/12") 
time.sleep(20)
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
# передаем в поле ответ
textarea.send_keys("get()")
time.sleep(5)
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
submit_button.click() 
time.sleep(5)
#закрыть окно браузера
driver.quit()
