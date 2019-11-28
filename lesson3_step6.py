from selenium import webdriver

import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
 
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()