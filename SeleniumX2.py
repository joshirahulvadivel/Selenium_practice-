from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

FirstnameText = driver.find_element(By.NAME, "firstname")
FirstnameText.send_keys("Alejandro")

SecondnameText = driver.find_element(By.NAME, "lastname")
SecondnameText.send_keys("Garnacho")

#GenderButton = driver.find_element(By.ID, "sex-0").click()

#ExselectButton = driver.find_elements(By.ID, "exp-2").click()

DatepickText = driver.find_element(By.ID, "datepicker")
DatepickText.send_keys("31/10/2023")

ProfessionButton = driver.find_element(By.ID, "profession-1").click()

ToolButton = driver.find_element(By.ID, "tool-2").click()


continentslist = Select(driver.find_element(By.ID, "continents"))
continentslist.select_by_visible_text("North America")

continentslist = Select(driver.find_element(By.ID, "selenium_commands"))
continentslist.select_by_visible_text("Browser Commands")

time.sleep(20)

