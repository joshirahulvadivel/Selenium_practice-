
#ex1
'''from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.youtube.com")


from selenium import webdriver
from selenium.webdriver.common.by import By
 
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

usernameFeild = driver.find_element(By.ID, "user-name")
usernameFeild.send_keys("Hello")
'''


#ex2
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time
 
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

usernameText = driver.find_element(By.ID, "username")
usernameText.send_keys("student")

PasswordText = driver.find_element(By.ID, "password")
PasswordText.send_keys("Password123")

LoginButtom = driver.find_element(By.ID, "submit").click()

time.sleep(10)

driver.quit()
'''

#hw 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time
 
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

usernameText = driver.find_element(By.ID, "user-name")
usernameText.send_keys("standard_user")

PasswordText = driver.find_element(By.ID, "password")
PasswordText.send_keys("secret_sauce")

LoginButtom = driver.find_element(By.ID, "login-button").click()



ProductElement = driver.find_elements(By.CLASS_NAME, "btn_inventory")

for element in ProductElement:
    # Perform actions on each element, for example, clicking
    element.click()
    time.sleep(1)  # Add a delay if needed

BuyingButton = driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(1)
CheckoutButton = driver.find_element(By.ID, "checkout").click()
time.sleep(1)

FirstnameText = driver.find_element(By.ID, "first-name")
FirstnameText.send_keys("James")
time.sleep(1)

LastnameText = driver.find_element(By.ID, "last-name")
LastnameText.send_keys("Bond")
time.sleep(1)

PostcodeText = driver.find_element(By.ID, "postal-code")
PostcodeText.send_keys("600011")
time.sleep(1)

ContinueButton = driver.find_element(By.ID, "continue").click()
time.sleep(1)

FinishButton = driver.find_element(By.ID, "finish").click()
time.sleep(1)


time.sleep(30)

driver.quit()