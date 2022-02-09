from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

service = webdriver.chrome.service.Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.instagram.com')
time.sleep(5)

my_id = input("email : ")
my_pw = input("pw : ")

id = driver.find_element(By.NAME, "username")
id.send_keys(my_id)
pw = driver.find_element(By.NAME, "password")
pw.send_keys(my_pw)
time.sleep(3)