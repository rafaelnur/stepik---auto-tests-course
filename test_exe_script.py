from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    
    
    # Ваш код, который заполняет обязательные поля
    browser.execute_script("window.scrollBy(0, 150);")
    input1 = browser.find_element_by_xpath("//*[@id='answer']")
    input1.send_keys(y)
    
    # Отправляем заполненную форму
    browser.execute_script("window.scrollBy(0, 150);")
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()

    browser.execute_script("window.scrollBy(0, 150);")    
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()

    browser.execute_script("window.scrollBy(0, 150);")    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()