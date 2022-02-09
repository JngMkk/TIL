from selenium import webdriver

driver = webdriver.chrome('/Users/JngMK/2021KNUpython2/chromedriver')

import time

driver.get('https://www.instagram.com')

time.sleep(2)

email = '01071370240'
input_id = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[0]
input_id.clear()
input_id.send_keys(email)

password = 'wndahek12@'
input_pw = driver.find_elements_by_css_selector('input._2hvTZ.pexuQ.zyHYP')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()
time.sleep(3)

name = 'rlaehrma'
input_search = driver.find_element_by_css_selector('input.XTCLo.x3qfX')
input_search.clear()
input_search.send_keys(name)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def insta_click(driver) :
    driver = driver.find_element_by_class_name('_7UhW9.xLCgt.qyrsm.KV-D4.uL8Hv') 
    driver.click()
    time.sleep(3)
insta_click(driver)

def select_first(driver):
    first = driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    time.sleep(3)
select_first(driver)

def click_like(driver):
    like = driver.find_elements_by_class_name('_8-yf5')
    like.click()
click_like(driver)

