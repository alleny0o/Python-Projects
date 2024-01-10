from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time

driver = webdriver.Chrome()

driver.get("https://cps-check.com/reaction-test")

WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((
    By.XPATH, '//div[@id="reaction"]')))

first_click = driver.find_element(
    By.XPATH, '//div[@id="reaction"]')
first_click.click()

WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located(
    (By.XPATH, '//div[@id="reaction-text"]/p[@class="r-main"]')))

while True:
    second_click = driver.find_element(
        By.XPATH, '//div[@id="reaction-text"]/p[@class="r-main"]')
    if second_click.text == "Click!":
        second_click.click()
        break

time.sleep(10)

driver.quit()
