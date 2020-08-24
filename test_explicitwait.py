from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)

input1 = browser.find_element_by_xpath("//*[@id='answer']")
input1.send_keys(y)

button = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )

button = browser.find_element_by_id("solve")
button.click()
time.sleep(1)
browser.quit