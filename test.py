from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://pypi.org/project/pytest/')
time.sleep(10)
browser.quit()
