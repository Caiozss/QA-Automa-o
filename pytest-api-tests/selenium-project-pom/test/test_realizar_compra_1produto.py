import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.saucedemo.com")


#fazendo login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#adicionando a mochila ao carrinho
driver.find_element(By.XPATH, "//*[@id='item_4_title_link']/div").click()
driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

#realizando o pagamento
driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a").click()
driver.find_element(By.XPATH, "//*[@id='checkout']").click()
driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("João")
driver.find_element(By.ID, "last-name").send_keys("Silva")
driver.find_element(By.XPATH,"//*[@id='postal-code']").send_keys("123456")
driver.find_element(By.XPATH,"//*[@id='continue']").click()
driver.find_element(By.XPATH, "//*[@id='finish']").click()
assert driver.find_element(By.XPATH,"//*[@id='checkout_complete_container']/h2").is_displayed()
